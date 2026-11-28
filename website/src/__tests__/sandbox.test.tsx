/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

import '@testing-library/jest-dom';
import { act } from 'react';
import { fireEvent, render, waitFor } from '@testing-library/react';
import Sandbox from '../sandbox/Sandbox';
import { SANDBOX_FILE_NAME } from '../pages/sandbox';
import { DEFAULT_SANDBOX_PROGRAM } from '../sandbox/DefaultSandboxProgram';
import { fetchPyreflyVersions } from '../sandbox/pyreflyVersions';
import { loadPyrefly } from '../sandbox/pyreflyWasmLoader';

// The version selector would fetch the version list from the network; the
// snapshot pins the sandbox while the list is still loading. The mock is
// countable so that tests can assert how often the catalog is requested.
jest.mock('../sandbox/pyreflyVersions', () => ({
    ...jest.requireActual('../sandbox/pyreflyVersions'),
    fetchPyreflyVersions: jest.fn(() => new Promise(() => {})),
}));

// The loader is mocked so that tests can drive version loads; the default
// implementation is the real one, which loads the bundled build.
jest.mock('../sandbox/pyreflyWasmLoader', () => {
    const actual = jest.requireActual('../sandbox/pyreflyWasmLoader');
    return {
        ...actual,
        loadPyrefly: jest.fn(),
    };
});

const actualLoader = jest.requireActual('../sandbox/pyreflyWasmLoader');
const loadPyreflyMock = loadPyrefly as unknown as jest.Mock;
const fetchVersionsMock = fetchPyreflyVersions as unknown as jest.Mock;

describe('Sandbox Component', () => {
    const pyreflyCommit = '123456789abcdef';

    beforeAll(() => {
        process.env.PYREFLY_COMMIT = pyreflyCommit;
    });

    afterAll(() => {
        delete process.env.PYREFLY_COMMIT;
    });

    beforeEach(() => {
        loadPyreflyMock.mockImplementation((version: string | null) =>
            actualLoader.loadPyrefly(version)
        );
        fetchVersionsMock.mockClear();
        fetchVersionsMock.mockImplementation(() => new Promise(() => {}));
    });

    afterEach(() => {
        window.history.replaceState({}, '', '/');
    });

    test('render sandbox correctly', async () => {
        const container = await act(async () => {
            const { container } = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );

            await Promise.resolve(); // Let any promises from timers resolve
            return container;
        });

        expectMonacoEditorLoadedWithContent(
            container,
            SANDBOX_FILE_NAME,
            DEFAULT_SANDBOX_PROGRAM,
            false
        );
        const buildLink = container.querySelector('#pyrefly-build');
        expect(buildLink).toHaveTextContent(
            'Pyrefly 1.2.3-test (commit 123456789)'
        );
        expect(buildLink).toHaveAttribute(
            'href',
            `https://github.com/pyrefly-org/pyrefly/commit/${pyreflyCommit}`
        );

        // Run test with --update-snapshot to update the snapshot if the test is failing after
        // you made a intentional change to the home page
        expect(container).toMatchSnapshot();
    });

    test('renders in code snippet mode without error panel', async () => {
        const fileName = 'snippet.py';
        const programContent = 'def hello(): pass';
        const container = await act(async () => {
            const { container } = render(
                <Sandbox
                    sampleFilename={fileName}
                    isCodeSnippet={true}
                    codeSample={programContent}
                />
            );

            await Promise.resolve(); // Let any promises from timers resolve
            return container;
        });

        expectMonacoEditorLoadedWithContent(
            container,
            fileName,
            programContent,
            true
        );

        // Run test with --update-snapshot to update the snapshot if the test is failing after
        // you made a intentional change to the home page
        expect(container).toMatchSnapshot();
    });

    test('toggles parameter name hints', async () => {
        const { getByLabelText } = await act(async () => {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await Promise.resolve();
            return result;
        });
        const toggle = getByLabelText('Parameter hints');

        expect(toggle).not.toBeChecked();
        fireEvent.click(toggle);
        expect(toggle).toBeChecked();
    });
    test('omits the commit for local builds', async () => {
        delete process.env.PYREFLY_COMMIT;
        try {
            const container = await act(async () => {
                const { container } = render(
                    <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
                );

                await Promise.resolve();
                return container;
            });

            expect(
                container.querySelector('#pyrefly-build')
            ).not.toBeInTheDocument();
        } finally {
            process.env.PYREFLY_COMMIT = pyreflyCommit;
        }
    });

    // Ordinary UI updates must not remount the selector into another
    // catalog fetch.
    test('does not refetch the version catalog on ordinary UI updates', async () => {
        const { getByLabelText } = await act(async () => {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await Promise.resolve();
            return result;
        });
        const fetchCount = fetchVersionsMock.mock.calls.length;
        expect(fetchCount).toBeGreaterThan(0);

        fireEvent.click(getByLabelText('Parameter hints'));
        await act(async () => {
            await Promise.resolve();
        });

        expect(fetchVersionsMock.mock.calls.length).toBe(fetchCount);
    });

    // A build that loads but rejects `State` must not become the reported
    // version: the selection and URL would claim a checker that never ran.
    test('falls back when a selected version cannot construct State', async () => {
        window.history.replaceState({}, '', '/?pyrefly=1.2.0');
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null
                ? actualLoader.loadPyrefly(version)
                : Promise.resolve({
                      mod: {
                          version: () => '1.2.0',
                          State: class {
                              constructor() {
                                  throw new Error('incompatible State');
                              }
                          },
                      },
                      wasmSource:
                          'https://example.invalid/pyrefly_wasm_bg.wasm',
                  })
        );

        const { getByLabelText } = await act(async () => {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await Promise.resolve();
            return result;
        });

        const selector = getByLabelText('Select Pyrefly version');
        await waitFor(() => expect(selector).toHaveValue(''));
        expect(window.location.search).not.toContain('pyrefly');
    });

    // The fallback explanation lives in its own state: the successful
    // bundled load that follows must not erase it.
    test('keeps the fallback warning visible after the bundled build loads', async () => {
        window.history.replaceState({}, '', '/?pyrefly=1.2.0');
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null
                ? actualLoader.loadPyrefly(version)
                : Promise.reject(new Error('network down'))
        );

        const { getByLabelText, getByText } = await act(async () => {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await Promise.resolve();
            return result;
        });

        await waitFor(() =>
            expect(getByLabelText('Select Pyrefly version')).toHaveValue('')
        );
        await waitFor(() =>
            expect(
                getByText(/Failed to load pyrefly 1\.2\.0/)
            ).toBeInTheDocument()
        );
    });

    // The URL is global: a load that outlives its sandbox must not write it.
    test('a stale load failure does not clear the URL of a later sandbox', async () => {
        window.history.replaceState({}, '', '/?pyrefly=2.0.0');
        let rejectLoad: (reason?: unknown) => void = () => {};
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null
                ? actualLoader.loadPyrefly(version)
                : new Promise((_resolve, reject) => {
                      rejectLoad = reject;
                  })
        );

        const { unmount } = await act(async () => {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await Promise.resolve();
            return result;
        });
        unmount();

        await act(async () => {
            rejectLoad(new Error('too late'));
            await Promise.resolve();
        });

        expect(window.location.search).toContain('pyrefly=2.0.0');
    });

    // These tests pin the transition behavior before changing checker ownership.
    test('reports the running build while a release is pending', async () => {
        const bundled = await actualLoader.loadPyrefly(null);
        let finishLoad!: (loaded: typeof bundled) => void;
        const pending = new Promise<typeof bundled>((resolve) => {
            finishLoad = resolve;
        });
        fetchVersionsMock.mockResolvedValue([
            { version: '1.5.0', prerelease: false },
        ]);
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null ? Promise.resolve(bundled) : pending
        );
        const open = jest.spyOn(window, 'open').mockImplementation(() => null);
        try {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            const selector = result.getByLabelText('Select Pyrefly version');
            await waitFor(() => expect(selector).not.toBeDisabled());
            await waitFor(() =>
                expect(selector).toHaveTextContent('Pyrefly 1.5.0')
            );
            fireEvent.change(selector, { target: { value: '1.5.0' } });
            // Bug: pending downloads hide results from the still-active checker.
            expect(result.queryByText('No errors!')).not.toBeInTheDocument();
            const link = result.container.querySelector('#pyrefly-build');
            expect(link).toHaveTextContent('Pyrefly 1.2.3-test');
            // Bug: the label still describes bundled, but its link and report URL do not.
            expect(link).toHaveAttribute(
                'href',
                'https://github.com/pyrefly-org/pyrefly/releases/tag/1.5.0'
            );
            fireEvent.click(result.getByLabelText('report issue on GitHub'));
            const issue = new URL(open.mock.calls[0][0] as string);
            expect(issue.searchParams.get('description')).toContain(
                'Pyrefly: 1.2.3-test'
            );
            expect(
                new URL(issue.searchParams.get('sandbox')!).searchParams.get(
                    'pyrefly'
                )
            ).toBe('1.5.0');
            await act(async () => {
                finishLoad({
                    ...bundled,
                    mod: { ...bundled.mod, version: () => '1.5.0' },
                });
            });
            expect(link).toHaveTextContent('Pyrefly 1.5.0');
            expect(
                new URLSearchParams(window.location.search).get('pyrefly')
            ).toBe('1.5.0');
        } finally {
            open.mockRestore();
        }
    });

    test('can return to bundled while a shared release is pending', async () => {
        window.history.replaceState({}, '', '/?pyrefly=1.5.0');
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null
                ? actualLoader.loadPyrefly(null)
                : new Promise(() => {})
        );
        const result = render(<Sandbox sampleFilename={SANDBOX_FILE_NAME} />);
        const selector = result.getByLabelText('Select Pyrefly version');
        await act(async () => {
            await Promise.resolve();
        });
        // Bug: the only control that can select the bundled build is disabled.
        expect(selector).toBeDisabled();
        expect(selector).toHaveValue('1.5.0');
    });

    test('recovers the running module rather than a pending release', async () => {
        const bundled = await actualLoader.loadPyrefly(null);
        let notReady = false;
        const bundledInit = jest.fn().mockResolvedValue(undefined);
        const releaseInit = jest.fn().mockResolvedValue(undefined);
        const running = {
            ...bundled,
            mod: {
                ...bundled.mod,
                default: bundledInit,
                State: class extends bundled.mod.State {
                    getErrors() {
                        if (notReady)
                            throw new Error('pyrefly_wasm is not ready');
                        return [];
                    }
                },
            },
        };
        let finishLoad!: (loaded: typeof bundled) => void;
        const pending = new Promise<typeof bundled>((resolve) => {
            finishLoad = resolve;
        });
        fetchVersionsMock.mockResolvedValue([
            { version: '1.5.0', prerelease: false },
        ]);
        loadPyreflyMock.mockImplementation((version: string | null) =>
            version === null ? Promise.resolve(running) : pending
        );
        const error = jest.spyOn(console, 'error').mockImplementation(() => {});
        try {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            const selector = result.getByLabelText('Select Pyrefly version');
            await waitFor(() => expect(selector).not.toBeDisabled());
            await waitFor(() =>
                expect(selector).toHaveTextContent('Pyrefly 1.5.0')
            );
            fireEvent.change(selector, { target: { value: '1.5.0' } });
            notReady = true;
            fireEvent.click(result.getByLabelText('Parameter hints'));
            notReady = false;
            await act(async () => {
                finishLoad({
                    ...bundled,
                    mod: {
                        ...bundled.mod,
                        default: releaseInit,
                        version: () => '1.5.0',
                    },
                });
            });
            // Bug: the pending loader promise selects the wrong module for recovery.
            expect(bundledInit).not.toHaveBeenCalled();
            expect(releaseInit).toHaveBeenCalledTimes(1);
        } finally {
            error.mockRestore();
        }
    });

    test('bundled initialization preserves the URL and router history entry', async () => {
        const state = { routerKey: 'sandbox-entry' };
        window.history.replaceState(
            state,
            '',
            '/?version=3.12#sandbox-results-container'
        );
        const replace = jest.spyOn(window.history, 'replaceState');
        try {
            const result = render(
                <Sandbox sampleFilename={SANDBOX_FILE_NAME} />
            );
            await waitFor(() =>
                expect(
                    result.container.querySelector('#pyrefly-build')
                ).toHaveTextContent('Pyrefly 1.2.3-test')
            );
            expect(window.location.hash).toBe('#sandbox-results-container');
            expect(window.history.state).toEqual(state);
            expect(replace).not.toHaveBeenCalled();
        } finally {
            replace.mockRestore();
        }
    });

    test('version controls have a row separate from file tabs', async () => {
        const result = render(<Sandbox sampleFilename={SANDBOX_FILE_NAME} />);
        const selector = result.getByLabelText('Select Pyrefly version');
        await waitFor(() => expect(selector).not.toBeDisabled());
        // Bug: file tabs consume the settings row's width on phones.
        expect(selector.parentElement).toHaveTextContent('sandbox.py');
    });

    function expectMonacoEditorLoadedWithContent(
        container: HTMLElement,
        fileName: string,
        programContent: string,
        isCodeSnippet: boolean
    ) {
        const sandboxEditorElement = container.querySelector('#sandbox-editor');
        expect(sandboxEditorElement).toBeInTheDocument();

        // Verify that the code editor container is a child of sandbox-editor
        const codeEditorContainer = sandboxEditorElement?.querySelector(
            '#sandbox-code-editor-container'
        );
        expect(codeEditorContainer).toBeInTheDocument();

        // Verify that the results container is a child of sandbox-editor
        const resultsContainer = sandboxEditorElement?.querySelector(
            '#sandbox-results-container'
        );
        if (isCodeSnippet) {
            expect(resultsContainer).not.toBeInTheDocument();
        } else {
            expect(resultsContainer).toBeInTheDocument();
        }

        // Verify that the Monaco editor is rendered
        const monacoEditor =
            codeEditorContainer.querySelector('#monaco-editor');
        expect(monacoEditor).toBeInTheDocument();

        // Verify that the editor has the correct path
        expect(monacoEditor.textContent).toContain(
            `Monaco Editor (Path: ${fileName})`
        );

        // Verify that the editor textarea is rendered
        const editorTextarea = monacoEditor.querySelector('#editor-textarea');
        expect(editorTextarea).toBeInTheDocument();

        // Verify that the editor content exactly matches the default Python program
        expect(editorTextarea).toHaveValue(programContent);

        // Verify that the share URL button exists
        const shareUrlButton =
            codeEditorContainer.querySelector('#share-url-button');
        if (isCodeSnippet) {
            expect(shareUrlButton).not.toBeInTheDocument();
        } else {
            expect(shareUrlButton).toBeInTheDocument();
        }
    }
});
