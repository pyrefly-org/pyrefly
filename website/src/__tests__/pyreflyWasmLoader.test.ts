/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

// The `pyrefly_wasm` import resolves to `__mocks__/pyreflyWasmMock.ts`, as
// configured for every test but `pyrefly_wasm.test.ts`.

import { loadPyrefly } from '../sandbox/pyreflyWasmLoader';
import { restoreFetch, stubFetch } from './__test_utils__/fetchStub';

describe('pyreflyWasmLoader', () => {
    test('loads the bundled build and caches it', async () => {
        const first = loadPyrefly(null);
        // A repeated load of the bundled build reuses the promise.
        expect(loadPyrefly(null)).toBe(first);
        const loaded = await first;
        // The bundled build resolves its `.wasm` file relative to itself.
        expect(loaded.wasmSource).toBeUndefined();
        expect(loaded.mod.version()).toBe('1.2.3-test');
    });

    // Versions reach the loader from shared URLs, so it is the trust
    // boundary: a crafted value must be rejected before any request.
    test('rejects an invalid version without fetching anything', async () => {
        const fetchMock = jest.fn();
        stubFetch(fetchMock);
        try {
            await expect(loadPyrefly('1/../evil-pkg@1.0.0')).rejects.toThrow(
                'Invalid pyrefly version'
            );
            await expect(loadPyrefly('1.2.0-../../evil')).rejects.toThrow(
                'Invalid pyrefly version'
            );
            expect(fetchMock).not.toHaveBeenCalled();
        } finally {
            restoreFetch();
        }
    });

    test('fetches the glue of a valid version from the package', async () => {
        const fetchMock = jest
            .fn()
            .mockResolvedValue({ ok: false, status: 404 });
        stubFetch(fetchMock);
        try {
            await expect(loadPyrefly('1.2.0')).rejects.toThrow('404');
            expect(fetchMock).toHaveBeenCalledWith(
                'https://cdn.jsdelivr.net/npm/pyrefly-wasm@1.2.0/pyrefly_wasm.js'
            );
        } finally {
            restoreFetch();
        }
    });
});
