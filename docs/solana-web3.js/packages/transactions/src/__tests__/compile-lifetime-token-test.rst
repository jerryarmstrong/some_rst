packages/transactions/src/__tests__/compile-lifetime-token-test.ts
==================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Blockhash } from '../blockhash';
import { getCompiledLifetimeToken } from '../compile-lifetime-token';
import { Nonce } from '../durable-nonce';

describe('getCompiledLifetimeToken', () => {
    it('compiles a recent blockhash lifetime constraint', () => {
        const token = getCompiledLifetimeToken({
            blockhash: 'abc' as Blockhash,
            lastValidBlockHeight: 100n,
        });
        expect(token).toBe('abc');
    });
    it('compiles a nonce lifetime constraint', () => {
        const token = getCompiledLifetimeToken({
            nonce: 'abc' as Nonce,
        });
        expect(token).toBe('abc');
    });
});


