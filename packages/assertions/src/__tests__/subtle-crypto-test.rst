packages/assertions/src/__tests__/subtle-crypto-test.ts
=======================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {
    assertDigestCapabilityIsAvailable,
    assertKeyExporterIsAvailable,
    assertSigningCapabilityIsAvailable,
    assertVerificationCapabilityIsAvailable,
} from '../subtle-crypto';

describe('assertDigestCapabilityIsAvailable()', () => {
    it('resolves to `undefined` without throwing', async () => {
        expect.assertions(1);
        await expect(assertDigestCapabilityIsAvailable()).resolves.toBeUndefined();
    });
    if (__BROWSER__) {
        describe('when in an insecure browser context', () => {
            beforeEach(() => {
                globalThis.isSecureContext = false;
            });
            it('rejects', async () => {
                expect.assertions(1);
                await expect(() => assertDigestCapabilityIsAvailable()).rejects.toThrow();
            });
        });
    }
    describe('when `SubtleCrypto::digest` is not available', () => {
        let oldDigest: InstanceType<typeof SubtleCrypto>['digest'];
        beforeEach(() => {
            oldDigest = globalThis.crypto.subtle.digest;
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.digest = undefined;
        });
        afterEach(() => {
            globalThis.crypto.subtle.digest = oldDigest;
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertDigestCapabilityIsAvailable()).rejects.toThrow();
        });
    });
});

describe('assertKeyExporterIsAvailable()', () => {
    it('resolves to `undefined` without throwing', async () => {
        expect.assertions(1);
        await expect(assertKeyExporterIsAvailable()).resolves.toBeUndefined();
    });
    if (__BROWSER__) {
        describe('when in an insecure browser context', () => {
            beforeEach(() => {
                globalThis.isSecureContext = false;
            });
            it('rejects', async () => {
                expect.assertions(1);
                await expect(() => assertKeyExporterIsAvailable()).rejects.toThrow();
            });
        });
    }
    describe('when `SubtleCrypto::exportKey` is not available', () => {
        let oldExportKey: InstanceType<typeof SubtleCrypto>['exportKey'];
        beforeEach(() => {
            oldExportKey = globalThis.crypto.subtle.exportKey;
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.exportKey = undefined;
        });
        afterEach(() => {
            globalThis.crypto.subtle.exportKey = oldExportKey;
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertKeyExporterIsAvailable()).rejects.toThrow();
        });
    });
});

describe('assertKeyGenerationIsAvailable()', () => {
    let assertKeyGenerationIsAvailable: typeof import('../subtle-crypto').assertKeyGenerationIsAvailable;
    beforeEach(async () => {
        await jest.isolateModulesAsync(async () => {
            const guardModulePromise =
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                import('../subtle-crypto');
            assertKeyGenerationIsAvailable = (await guardModulePromise).assertKeyGenerationIsAvailable;
        });
    });
    it('resolves to `undefined` without throwing', async () => {
        expect.assertions(1);
        await expect(assertKeyGenerationIsAvailable()).resolves.toBeUndefined();
    });
    if (__BROWSER__) {
        describe('when in an insecure browser context', () => {
            beforeEach(() => {
                globalThis.isSecureContext = false;
            });
            it('rejects', async () => {
                expect.assertions(1);
                await expect(() => assertKeyGenerationIsAvailable()).rejects.toThrow();
            });
        });
    }
    describe('when `SubtleCrypto::generateKey` is not available', () => {
        let oldGenerateKey: InstanceType<typeof SubtleCrypto>['generateKey'];
        beforeEach(() => {
            oldGenerateKey = globalThis.crypto.subtle.generateKey;
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.generateKey = undefined;
        });
        afterEach(() => {
            globalThis.crypto.subtle.generateKey = oldGenerateKey;
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertKeyGenerationIsAvailable()).rejects.toThrow();
        });
    });
    describe('when the Ed25519 curve is not available', () => {
        beforeEach(() => {
            const oldGenerateKey = globalThis.crypto.subtle.generateKey;
            jest.spyOn(globalThis.crypto.subtle, 'generateKey').mockImplementation(async (algorithm, ...rest) => {
                if (algorithm === 'Ed25519') {
                    throw new Error('Ed25519 not supported');
                }
                return await oldGenerateKey.call(globalThis.crypto.subtle, algorithm, ...rest);
            });
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertKeyGenerationIsAvailable()).rejects.toThrow();
        });
        it('remembers the result from the first time it is called (parallel checks)', async () => {
            expect.assertions(1);
            try {
                await Promise.all([assertKeyGenerationIsAvailable(), assertKeyGenerationIsAvailable()]);
            } catch {
                /* empty */
            }
            expect(globalThis.crypto.subtle.generateKey).toHaveBeenCalledTimes(1);
        });
        it('remembers the result from the first time it is called (serial checks)', async () => {
            expect.assertions(1);
            try {
                await assertKeyGenerationIsAvailable();
                await assertKeyGenerationIsAvailable();
            } catch {
                /* empty */
            }
            expect(globalThis.crypto.subtle.generateKey).toHaveBeenCalledTimes(1);
        });
    });
});

describe('assertSigningCapabilityIsAvailable()', () => {
    it('resolves to `undefined` without throwing', async () => {
        expect.assertions(1);
        await expect(assertSigningCapabilityIsAvailable()).resolves.toBeUndefined();
    });
    if (__BROWSER__) {
        describe('when in an insecure browser context', () => {
            beforeEach(() => {
                globalThis.isSecureContext = false;
            });
            it('rejects', async () => {
                expect.assertions(1);
                await expect(() => assertSigningCapabilityIsAvailable()).rejects.toThrow();
            });
        });
    }
    describe('when `SubtleCrypto::sign` is not available', () => {
        let oldSign: InstanceType<typeof SubtleCrypto>['sign'];
        beforeEach(() => {
            oldSign = globalThis.crypto.subtle.sign;
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.sign = undefined;
        });
        afterEach(() => {
            globalThis.crypto.subtle.sign = oldSign;
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertSigningCapabilityIsAvailable()).rejects.toThrow();
        });
    });
});

describe('assertVerificationCapabilityIsAvailable()', () => {
    it('resolves to `undefined` without throwing', async () => {
        expect.assertions(1);
        await expect(assertVerificationCapabilityIsAvailable()).resolves.toBeUndefined();
    });
    if (__BROWSER__) {
        describe('when in an insecure browser context', () => {
            beforeEach(() => {
                globalThis.isSecureContext = false;
            });
            it('rejects', async () => {
                expect.assertions(1);
                await expect(() => assertVerificationCapabilityIsAvailable()).rejects.toThrow();
            });
        });
    }
    describe('when `SubtleCrypto::sign` is not available', () => {
        let oldVerify: InstanceType<typeof SubtleCrypto>['verify'];
        beforeEach(() => {
            oldVerify = globalThis.crypto.subtle.verify;
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.verify = undefined;
        });
        afterEach(() => {
            globalThis.crypto.subtle.verify = oldVerify;
        });
        it('rejects', async () => {
            expect.assertions(1);
            await expect(assertVerificationCapabilityIsAvailable()).rejects.toThrow();
        });
    });
});


