packages/library/src/rpc-default-config.ts
==========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { createSolanaRpcApi } from '@solana/rpc-core';

import { SolanaJsonRpcIntegerOverflowError } from './rpc-integer-overflow-error';

export const DEFAULT_RPC_CONFIG: Partial<Parameters<typeof createSolanaRpcApi>[0]> = {
    onIntegerOverflow(methodName, keyPath, value) {
        throw new SolanaJsonRpcIntegerOverflowError(methodName, keyPath, value);
    },
};


