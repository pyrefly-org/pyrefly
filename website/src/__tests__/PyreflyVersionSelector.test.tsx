/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

import '@testing-library/jest-dom';
import { fireEvent, render, waitFor } from '@testing-library/react';
import React from 'react';
import PyreflyVersionSelector from '../sandbox/PyreflyVersionSelector';
import { invalidatePyreflyVersions } from '../sandbox/pyreflyVersions';
import { restoreFetch, stubFetch } from './__test_utils__/fetchStub';

const VERSIONS_RESPONSE = {
    versions: [
        { version: '1.2.0' },
        { version: '1.1.0' },
        { version: '1.2.0-dev.2' },
    ],
};

describe('PyreflyVersionSelector', () => {
    const originalReleaseFlag = process.env.PYREFLY_WASM_RELEASES_ENABLED;
    beforeEach(() => {
        process.env.PYREFLY_WASM_RELEASES_ENABLED = '1';
        invalidatePyreflyVersions();
    });

    afterEach(() => {
        restoreFetch();
        if (originalReleaseFlag === undefined) {
            delete process.env.PYREFLY_WASM_RELEASES_ENABLED;
        } else {
            process.env.PYREFLY_WASM_RELEASES_ENABLED = originalReleaseFlag;
        }
    });

    test('lists releases and dev builds and reports the selection', async () => {
        stubFetch(
            jest.fn().mockResolvedValue({
                ok: true,
                json: async () => VERSIONS_RESPONSE,
            })
        );
        const onSelect = jest.fn();
        const { getByLabelText } = render(
            <PyreflyVersionSelector
                selected={null}
                onSelect={onSelect}
                disabled={false}
            />
        );
        const selector = getByLabelText('Select Pyrefly version');
        await waitFor(() =>
            expect(selector).toHaveTextContent('Pyrefly 1.2.0')
        );
        // Releases sort newest first, and dev builds come after them.
        expect(selector).toHaveTextContent('Pyrefly 1.1.0');
        expect(selector).toHaveTextContent('Pyrefly 1.2.0-dev.2');

        fireEvent.change(selector, { target: { value: '1.2.0' } });
        expect(onSelect).toHaveBeenCalledWith('1.2.0');
        // The empty value selects the bundled build.
        fireEvent.change(selector, { target: { value: '' } });
        expect(onSelect).toHaveBeenCalledWith(null);
    });

    test('keeps a selected version that the list does not know', async () => {
        stubFetch(
            jest.fn().mockResolvedValue({
                ok: true,
                json: async () => VERSIONS_RESPONSE,
            })
        );
        const onSelect = jest.fn();
        const { getByLabelText } = render(
            <PyreflyVersionSelector
                selected="9.9.9"
                onSelect={onSelect}
                disabled={false}
            />
        );
        const selector = getByLabelText('Select Pyrefly version');
        expect(selector).toHaveValue('9.9.9');
        await waitFor(() =>
            expect(selector).toHaveTextContent('Pyrefly 1.2.0')
        );
        expect(selector).toHaveValue('9.9.9');
    });

    test('serves a remount from the cached list', async () => {
        const fetchMock = jest.fn().mockResolvedValue({
            ok: true,
            json: async () => VERSIONS_RESPONSE,
        });
        stubFetch(fetchMock);
        const { unmount, getByLabelText } = render(
            <PyreflyVersionSelector
                selected={null}
                onSelect={jest.fn()}
                disabled={false}
            />
        );
        const selector = getByLabelText('Select Pyrefly version');
        await waitFor(() =>
            expect(selector).toHaveTextContent('Pyrefly 1.2.0')
        );
        unmount();

        // A remount (an ordinary parent re-render) reuses the one request.
        const second = render(
            <PyreflyVersionSelector
                selected={null}
                onSelect={jest.fn()}
                disabled={false}
            />
        );
        await waitFor(() =>
            expect(
                second.getByLabelText('Select Pyrefly version')
            ).toHaveTextContent('Pyrefly 1.2.0')
        );
        expect(fetchMock).toHaveBeenCalledTimes(1);
    });

    test('falls back to the bundled build when the list fails', async () => {
        // The rejection is created per call, so that the stub never leaves
        // an unhandled rejection behind.
        stubFetch(
            jest
                .fn()
                .mockImplementation(() => Promise.reject(new Error('offline')))
        );
        const onSelect = jest.fn();
        const { getByLabelText } = render(
            <PyreflyVersionSelector
                selected={null}
                onSelect={onSelect}
                disabled={false}
            />
        );
        const selector = getByLabelText('Select Pyrefly version');
        await waitFor(() =>
            expect(selector).toHaveAttribute(
                'title',
                'The Pyrefly version list is unavailable'
            )
        );
        // Only the bundled build remains selectable.
        expect(selector).not.toHaveTextContent('Pyrefly 1.');
        fireEvent.change(selector, { target: { value: '' } });
        expect(onSelect).toHaveBeenCalledWith(null);
    });
});
