packages/rpc-core/src/__tests__/stringified-bigint-test.ts
==========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { assertIsStringifiedBigInt } from '../stringified-bigint';

describe('assertIsStringifiedBigInt()', () => {
    it("throws when supplied a string that can't parse as a number", () => {
        expect(() => {
            assertIsStringifiedBigInt('abc');
        }).toThrow();
        expect(() => {
            assertIsStringifiedBigInt('123a');
        }).toThrow();
    });
    it("throws when supplied a string that can't parse as an integer", () => {
        expect(() => {
            assertIsStringifiedBigInt('123.0');
        }).toThrow();
        expect(() => {
            assertIsStringifiedBigInt('123.5');
        }).toThrow();
    });
    it('does not throw when supplied a string that parses as an integer', () => {
        expect(() => {
            assertIsStringifiedBigInt('-123');
        }).not.toThrow();
        expect(() => {
            assertIsStringifiedBigInt('0');
        }).not.toThrow();
        expect(() => {
            assertIsStringifiedBigInt('123');
        }).not.toThrow();
    });
});


