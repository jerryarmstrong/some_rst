packages/webcrypto-ed25519-polyfill/src/__tests__/index-test.ts
===============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { exportKeyPolyfill, generateKeyPolyfill, isPolyfilledKey, signPolyfill, verifyPolyfill } from '../secrets';

jest.mock('../secrets');

describe('exportKey() polyfill', () => {
    let originalExportKey: SubtleCrypto['exportKey'];
    beforeEach(() => {
        jest.spyOn(globalThis.crypto?.subtle, 'exportKey');
        originalExportKey = globalThis.crypto?.subtle?.exportKey;
    });
    afterEach(() => {
        globalThis.crypto.subtle.exportKey = originalExportKey;
    });
    describe('when imported', () => {
        beforeEach(() => {
            jest.isolateModules(() => {
                require('../index');
            });
        });
        it('delegates `exportKey` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPublicKey = {} as CryptoKey;
            await globalThis.crypto.subtle.exportKey('raw', mockPublicKey);
            expect(exportKeyPolyfill).toHaveBeenCalledWith('raw', mockPublicKey);
        });
        it('delegates `exportKey` calls to the original implementation when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPublicKey = {} as CryptoKey;
            try {
                // This will fail because the key is a mock. We are only interested in whether the
                // native implementation was *called* so this is OK.
                await globalThis.crypto.subtle.exportKey('raw', mockPublicKey);
            } catch {
                /* empty */
            }
            expect(originalExportKey).toHaveBeenCalledWith('raw', mockPublicKey);
        });
        it('overrides `exportKey`', () => {
            expect(globalThis.crypto.subtle.exportKey).not.toBe(originalExportKey);
        });
    });
    describe('when imported with no `exportKey` function', () => {
        beforeEach(() => {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.exportKey = undefined;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        afterEach(() => {
            globalThis.crypto.subtle.exportKey = originalExportKey;
        });
        it('delegates `exportKey` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPublicKey = {} as CryptoKey;
            await globalThis.crypto.subtle.exportKey('raw', mockPublicKey);
            expect(exportKeyPolyfill).toHaveBeenCalledWith('raw', mockPublicKey);
        });
        it('fatals when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPublicKey = {} as CryptoKey;
            await expect(() => globalThis.crypto.subtle.exportKey('raw', mockPublicKey)).rejects.toThrow();
        });
    });
    describe('when imported in an insecure context', () => {
        beforeEach(() => {
            globalThis.isSecureContext = false;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        if (__BROWSER__) {
            it('does not override `exportKey`', () => {
                expect(globalThis.crypto.subtle.exportKey).toBe(originalExportKey);
            });
        } else {
            it('overrides `exportKey`', () => {
                expect(globalThis.crypto.subtle.exportKey).not.toBe(originalExportKey);
            });
        }
    });
});

describe('generateKey() polyfill', () => {
    let originalGenerateKey: SubtleCrypto['generateKey'];
    beforeEach(() => {
        jest.spyOn(globalThis.crypto?.subtle, 'generateKey');
        originalGenerateKey = globalThis.crypto?.subtle?.generateKey;
    });
    afterEach(() => {
        globalThis.crypto.subtle.generateKey = originalGenerateKey;
    });
    describe('when imported in an environment with no `generateKey` function', () => {
        beforeEach(() => {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.generateKey = undefined;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        afterEach(() => {
            globalThis.crypto.subtle.generateKey = originalGenerateKey;
        });
        it.each([
            { __variant: 'P256', name: 'ECDSA', namedCurve: 'P-256' },
            { __variant: 'P384', name: 'ECDSA', namedCurve: 'P-384' } as EcKeyGenParams,
            { __variant: 'P521', name: 'ECDSA', namedCurve: 'P-521' } as EcKeyGenParams,
            ...['RSASSA-PKCS1-v1_5', 'RSA-PSS'].flatMap(rsaAlgoName =>
                ['SHA-1', 'SHA-256', 'SHA-384', 'SHA-512'].map(
                    hashName =>
                        ({
                            __variant: hashName,
                            hash: { name: hashName },
                            modulusLength: 2048,
                            name: rsaAlgoName,
                            publicExponent: new Uint8Array([0x01, 0x00, 0x01]),
                        } as RsaHashedKeyGenParams)
                )
            ),
        ])('fatals when the algorithm is $name/$__variant', async algorithm => {
            expect.assertions(1);
            await expect(() =>
                globalThis.crypto.subtle.generateKey(algorithm, /* extractable */ false, ['sign', 'verify'])
            ).rejects.toThrow();
        });
        it('delegates Ed25519 `generateKey` calls to the polyfill', async () => {
            expect.assertions(1);
            const mockKeyPair = {};
            (generateKeyPolyfill as jest.Mock).mockReturnValue(mockKeyPair);
            const keyPair = await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, [
                'sign',
                'verify',
            ]);
            expect(keyPair).toBe(mockKeyPair);
        });
    });
    describe('when imported in an environment that does not support Ed25519', () => {
        beforeEach(() => {
            const originalGenerateKeyImpl = originalGenerateKey;
            (originalGenerateKey as jest.Mock).mockImplementation(async (...args) => {
                const [algorithm] = args;
                if (algorithm === 'Ed25519') {
                    throw new Error('Ed25519 not supported');
                }
                return await originalGenerateKeyImpl.apply(globalThis.crypto.subtle, args);
            });
            jest.isolateModules(() => {
                require('../index');
            });
        });
        it('calls the original `generateKey` once as a test when the algorithm is "Ed25519" but never again (parallel version)', async () => {
            expect.assertions(1);
            await Promise.all([
                globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']),
                globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']),
            ]);
            expect(originalGenerateKey).toHaveBeenCalledTimes(1);
        });
        it('calls the original `generateKey` once as a test when the algorithm is "Ed25519" but never again (serial version)', async () => {
            expect.assertions(1);
            await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']);
            await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']);
            expect(originalGenerateKey).toHaveBeenCalledTimes(1);
        });
        it('delegates Ed25519 `generateKey` calls to the polyfill', async () => {
            expect.assertions(1);
            const mockKeyPair = {};
            (generateKeyPolyfill as jest.Mock).mockReturnValue(mockKeyPair);
            const keyPair = await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, [
                'sign',
                'verify',
            ]);
            expect(keyPair).toBe(mockKeyPair);
        });
    });
    describe('when imported in an environment that supports Ed25519', () => {
        beforeEach(() => {
            jest.isolateModules(() => {
                require('../index');
            });
        });
        it('overrides `generateKey`', () => {
            expect(globalThis.crypto.subtle.generateKey).not.toBe(originalGenerateKey);
        });
        it.each([
            { __variant: 'P256', name: 'ECDSA', namedCurve: 'P-256' },
            { __variant: 'P384', name: 'ECDSA', namedCurve: 'P-384' } as EcKeyGenParams,
            { __variant: 'P521', name: 'ECDSA', namedCurve: 'P-521' } as EcKeyGenParams,
            ...['RSASSA-PKCS1-v1_5', 'RSA-PSS'].flatMap(rsaAlgoName =>
                ['SHA-1', 'SHA-256', 'SHA-384', 'SHA-512'].map(
                    hashName =>
                        ({
                            __variant: hashName,
                            hash: { name: hashName },
                            modulusLength: 2048,
                            name: rsaAlgoName,
                            publicExponent: new Uint8Array([0x01, 0x00, 0x01]),
                        } as RsaHashedKeyGenParams)
                )
            ),
        ])('calls the original `generateKey` when the algorithm is $name/$__variant', async algorithm => {
            expect.assertions(1);
            await globalThis.crypto.subtle.generateKey(algorithm, /* extractable */ false, ['sign', 'verify']);
            expect(originalGenerateKey).toHaveBeenCalled();
        });
        it('delegates the call to the original `generateKey` when the algorithm is "Ed25519"', async () => {
            expect.assertions(1);
            const mockKeyPair = {};
            (originalGenerateKey as jest.Mock).mockResolvedValue(mockKeyPair);
            await expect(
                globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify'])
            ).resolves.toBe(mockKeyPair);
        });
        it('calls the original `generateKey` once per call to `generateKey` when the algorithm is "Ed25519" (parallel version)', async () => {
            expect.assertions(1);
            await Promise.all([
                globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']),
                globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']),
            ]);
            expect(originalGenerateKey).toHaveBeenCalledTimes(2);
        });
        it('calls the original `generateKey` once per call to `generateKey` when the algorithm is "Ed25519" (serial version)', async () => {
            expect.assertions(1);
            await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']);
            await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']);
            expect(originalGenerateKey).toHaveBeenCalledTimes(2);
        });
        it('does not delegate `generateKey` calls to the polyfill', async () => {
            expect.assertions(1);
            await globalThis.crypto.subtle.generateKey('Ed25519', /* extractable */ false, ['sign', 'verify']);
            expect(generateKeyPolyfill).not.toHaveBeenCalled();
        });
    });
    describe('when imported in an insecure context', () => {
        beforeEach(() => {
            globalThis.isSecureContext = false;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        if (__BROWSER__) {
            it('does not override `generateKey`', () => {
                expect(globalThis.crypto.subtle.generateKey).toBe(originalGenerateKey);
            });
        } else {
            it('overrides `generateKey`', () => {
                expect(globalThis.crypto.subtle.generateKey).not.toBe(originalGenerateKey);
            });
        }
    });
});

describe('sign() polyfill', () => {
    let originalSign: SubtleCrypto['sign'];
    beforeEach(() => {
        jest.spyOn(globalThis.crypto?.subtle, 'sign');
        originalSign = globalThis.crypto?.subtle?.sign;
    });
    afterEach(() => {
        globalThis.crypto.subtle.sign = originalSign;
    });
    describe('when imported', () => {
        beforeEach(() => {
            jest.isolateModules(() => {
                require('../index');
            });
        });
        it('delegates `sign` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            await globalThis.crypto.subtle.sign('Ed25519', mockPrivateKey, mockData);
            expect(signPolyfill).toHaveBeenCalledWith(mockPrivateKey, mockData);
        });
        it('delegates `sign` calls to the original implementation when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            try {
                // This will fail because the key is a mock. We are only interested in whether the
                // native implementation was *called* so this is OK.
                await globalThis.crypto.subtle.sign('Ed25519', mockPrivateKey, mockData);
            } catch {
                /* empty */
            }
            expect(originalSign).toHaveBeenCalledWith('Ed25519', mockPrivateKey, mockData);
        });
        it('overrides `sign`', () => {
            expect(globalThis.crypto.subtle.sign).not.toBe(originalSign);
        });
    });
    describe('when imported with no `sign` function', () => {
        beforeEach(() => {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.sign = undefined;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        afterEach(() => {
            globalThis.crypto.subtle.sign = originalSign;
        });
        it('delegates `sign` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            await globalThis.crypto.subtle.sign('Ed25519', mockPrivateKey, mockData);
            expect(signPolyfill).toHaveBeenCalledWith(mockPrivateKey, mockData);
        });
        it('fatals when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            await expect(() => globalThis.crypto.subtle.sign('Ed25519', mockPrivateKey, mockData)).rejects.toThrow();
        });
    });
    describe('when imported in an insecure context', () => {
        beforeEach(() => {
            globalThis.isSecureContext = false;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        if (__BROWSER__) {
            it('does not override `exportKey`', () => {
                expect(globalThis.crypto.subtle.sign).toBe(originalSign);
            });
        } else {
            it('overrides `exportKey`', () => {
                expect(globalThis.crypto.subtle.sign).not.toBe(originalSign);
            });
        }
    });
});

describe('verify() polyfill', () => {
    let originalVerify: SubtleCrypto['verify'];
    beforeEach(() => {
        jest.spyOn(globalThis.crypto?.subtle, 'verify');
        originalVerify = globalThis.crypto?.subtle?.verify;
    });
    afterEach(() => {
        globalThis.crypto.subtle.verify = originalVerify;
    });
    describe('when imported', () => {
        beforeEach(() => {
            jest.isolateModules(() => {
                require('../index');
            });
        });
        it('delegates `verify` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            const mockSignature = new Uint8Array(Array(64).fill(1));
            await globalThis.crypto.subtle.verify('Ed25519', mockPrivateKey, mockSignature, mockData);
            expect(verifyPolyfill).toHaveBeenCalledWith(mockPrivateKey, mockSignature, mockData);
        });
        it('delegates `verify` calls to the original implementation when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            const mockSignature = new Uint8Array(Array(64).fill(1));
            try {
                // This will fail because the key is a mock. We are only interested in whether the
                // native implementation was *called* so this is OK.
                await globalThis.crypto.subtle.verify('Ed25519', mockPrivateKey, mockSignature, mockData);
            } catch {
                /* empty */
            }
            expect(originalVerify).toHaveBeenCalledWith('Ed25519', mockPrivateKey, mockSignature, mockData);
        });
        it('overrides `verify`', () => {
            expect(globalThis.crypto.subtle.verify).not.toBe(originalVerify);
        });
    });
    describe('when imported with no `verify` function', () => {
        beforeEach(() => {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            globalThis.crypto.subtle.verify = undefined;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        afterEach(() => {
            globalThis.crypto.subtle.verify = originalVerify;
        });
        it('delegates `verify` calls to the polyfill when supplied a polyfill-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(true);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            const mockSignature = new Uint8Array(Array(64).fill(1));
            await globalThis.crypto.subtle.verify('Ed25519', mockPrivateKey, mockSignature, mockData);
            expect(verifyPolyfill).toHaveBeenCalledWith(mockPrivateKey, mockSignature, mockData);
        });
        it('fatals when supplied a native-generated key', async () => {
            expect.assertions(1);
            (isPolyfilledKey as jest.Mock).mockReturnValue(false);
            const mockPrivateKey = {} as CryptoKey;
            const mockData = new Uint8Array([1, 2, 3]);
            const mockSignature = new Uint8Array(Array(64).fill(1));
            await expect(() =>
                globalThis.crypto.subtle.verify('Ed25519', mockPrivateKey, mockSignature, mockData)
            ).rejects.toThrow();
        });
    });
    describe('when imported in an insecure context', () => {
        beforeEach(() => {
            globalThis.isSecureContext = false;
            jest.isolateModules(() => {
                require('../index');
            });
        });
        if (__BROWSER__) {
            it('does not override `exportKey`', () => {
                expect(globalThis.crypto.subtle.verify).toBe(originalVerify);
            });
        } else {
            it('overrides `exportKey`', () => {
                expect(globalThis.crypto.subtle.verify).not.toBe(originalVerify);
            });
        }
    });
});


