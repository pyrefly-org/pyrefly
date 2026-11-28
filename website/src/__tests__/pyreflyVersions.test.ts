/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

import {
    compareVersions,
    fetchPyreflyVersions,
    invalidatePyreflyVersions,
    isPrerelease,
    isValidPyreflyVersion,
    parsePyreflyVersions,
    pyreflyWasmUrls,
} from '../sandbox/pyreflyVersions';
import { restoreFetch, stubFetch } from './__test_utils__/fetchStub';

describe('pyreflyVersions', () => {
    const originalReleaseFlag = process.env.PYREFLY_WASM_RELEASES_ENABLED;
    // The catalog is cached across calls; each test needs its own fetch.
    beforeEach(() => {
        process.env.PYREFLY_WASM_RELEASES_ENABLED = '1';
        invalidatePyreflyVersions();
    });
    afterEach(() => {
        if (originalReleaseFlag === undefined) {
            delete process.env.PYREFLY_WASM_RELEASES_ENABLED;
        } else {
            process.env.PYREFLY_WASM_RELEASES_ENABLED = originalReleaseFlag;
        }
    });
    test('does not fetch a catalog until release publishing is enabled', async () => {
        delete process.env.PYREFLY_WASM_RELEASES_ENABLED;
        const fetchMock = jest
            .fn()
            .mockResolvedValue({ ok: false, status: 404 });
        stubFetch(fetchMock);
        try {
            // Bug: an absent publishing prerequisite does not prevent a request.
            await expect(fetchPyreflyVersions()).rejects.toThrow('404');
            expect(fetchMock).toHaveBeenCalledTimes(1);
        } finally {
            restoreFetch();
        }
    });
    test('pyreflyWasmUrls builds jsDelivr URLs', () => {
        expect(pyreflyWasmUrls('1.2.0')).toEqual({
            glue: 'https://cdn.jsdelivr.net/npm/pyrefly-wasm@1.2.0/pyrefly_wasm.js',
            wasm: 'https://cdn.jsdelivr.net/npm/pyrefly-wasm@1.2.0/pyrefly_wasm_bg.wasm',
        });
    });

    test('isPrerelease', () => {
        expect(isPrerelease('1.2.0')).toBe(false);
        expect(isPrerelease('1.2.0-dev.2')).toBe(true);
        expect(isPrerelease('1.2.0-rc.1')).toBe(true);
        // Build metadata does not make a prerelease.
        expect(isPrerelease('1.2.0+build')).toBe(false);
    });

    test('compareVersions orders semver', () => {
        expect(compareVersions('1.2.0', '1.1.9')).toBeGreaterThan(0);
        expect(compareVersions('1.10.0', '1.9.0')).toBeGreaterThan(0);
        expect(compareVersions('1.2.0', '1.2.0')).toBe(0);
        // A missing segment is zero.
        expect(compareVersions('1.2', '1.2.0')).toBe(0);
        // Prereleases sort before their release, and numerically.
        expect(compareVersions('1.2.0', '1.2.0-dev.2')).toBeGreaterThan(0);
        expect(compareVersions('1.2.0-dev.2', '1.2.0-dev.10')).toBeLessThan(0);
        // A longer prerelease sorts later.
        expect(compareVersions('1.2.0-dev.2', '1.2.0-dev')).toBeGreaterThan(0);
        // Numeric identifiers sort before alphanumeric ones.
        expect(compareVersions('1.2.0-dev.2', '1.2.0-alpha')).toBeGreaterThan(
            0
        );
        expect(compareVersions('1.2.0-2', '1.2.0-alpha')).toBeLessThan(0);
    });

    test('parsePyreflyVersions sorts and groups', () => {
        expect(
            parsePyreflyVersions({
                versions: [
                    { version: '1.0.0' },
                    { version: '1.2.0-dev.2' },
                    { version: '1.1.0' },
                    { version: '1.2.0-dev.1' },
                    { version: 'not-a-version' },
                    { version: '1.1.0+build' },
                ],
            })
        ).toEqual([
            // `1.1.0+build` compares equal to `1.1.0` (build metadata is
            // ignored), so the stable sort keeps the input order.
            { version: '1.1.0', prerelease: false },
            { version: '1.1.0+build', prerelease: false },
            { version: '1.0.0', prerelease: false },
            { version: '1.2.0-dev.2', prerelease: true },
            { version: '1.2.0-dev.1', prerelease: true },
        ]);
    });

    test('parsePyreflyVersions caps the list', () => {
        const stable = [];
        const prereleases = [];
        for (let minor = 0; minor < 20; minor++) {
            stable.push({ version: `1.${minor}.0` });
            prereleases.push({ version: `2.${minor}.0-dev.1` });
        }
        const parsed = parsePyreflyVersions({
            versions: [...stable, ...prereleases],
        });
        expect(parsed.filter((info) => !info.prerelease)).toHaveLength(15);
        expect(parsed.filter((info) => info.prerelease)).toHaveLength(10);
    });

    test('isValidPyreflyVersion accepts only complete npm versions', () => {
        expect(isValidPyreflyVersion('1.2.0')).toBe(true);
        expect(isValidPyreflyVersion('1.2.0-dev.2')).toBe(true);
        expect(isValidPyreflyVersion('1.2.0+build')).toBe(true);
        // Path traversal must not survive into the CDN URL.
        expect(isValidPyreflyVersion('1/../evil-pkg@1.0.0')).toBe(false);
        expect(isValidPyreflyVersion('1.2.0-../../evil')).toBe(false);
        expect(isValidPyreflyVersion('1.2')).toBe(false);
        expect(isValidPyreflyVersion('')).toBe(false);
    });

    test('parsePyreflyVersions tolerates a malformed response', () => {
        expect(parsePyreflyVersions(null)).toEqual([]);
        expect(parsePyreflyVersions({})).toEqual([]);
        expect(parsePyreflyVersions({ versions: 'oops' })).toEqual([]);
        // A traversal attempt is not a version and is dropped.
        expect(
            parsePyreflyVersions({
                versions: [{ version: '1.2.0-../../evil' }],
            })
        ).toEqual([]);
    });

    test('fetchPyreflyVersions parses the jsDelivr data API', async () => {
        const fetchMock = jest.fn().mockResolvedValue({
            ok: true,
            json: async () => ({ versions: [{ version: '1.2.0' }] }),
        });
        stubFetch(fetchMock);
        try {
            await expect(fetchPyreflyVersions()).resolves.toEqual([
                { version: '1.2.0', prerelease: false },
            ]);
            expect(fetchMock).toHaveBeenCalledWith(
                'https://data.jsdelivr.com/v1/packages/npm/pyrefly-wasm'
            );
        } finally {
            restoreFetch();
        }
    });

    test('fetchPyreflyVersions rejects on an error status', async () => {
        stubFetch(jest.fn().mockResolvedValue({ ok: false, status: 503 }));
        try {
            await expect(fetchPyreflyVersions()).rejects.toThrow('503');
        } finally {
            restoreFetch();
        }
    });

    test('fetchPyreflyVersions serves one request to every caller', async () => {
        const fetchMock = jest.fn().mockResolvedValue({
            ok: true,
            json: async () => ({ versions: [{ version: '1.2.0' }] }),
        });
        stubFetch(fetchMock);
        try {
            const first = fetchPyreflyVersions();
            const second = fetchPyreflyVersions();
            expect(second).toBe(first);
            await expect(first).resolves.toEqual([
                { version: '1.2.0', prerelease: false },
            ]);
            expect(fetchMock).toHaveBeenCalledTimes(1);
        } finally {
            restoreFetch();
        }
    });

    test('fetchPyreflyVersions retries after a failed request', async () => {
        const fetchMock = jest
            .fn()
            .mockResolvedValueOnce({ ok: false, status: 503 })
            .mockResolvedValueOnce({ ok: true, json: async () => ({}) });
        stubFetch(fetchMock);
        try {
            await expect(fetchPyreflyVersions()).rejects.toThrow('503');
            await expect(fetchPyreflyVersions()).resolves.toEqual([]);
            expect(fetchMock).toHaveBeenCalledTimes(2);
        } finally {
            restoreFetch();
        }
    });
});
