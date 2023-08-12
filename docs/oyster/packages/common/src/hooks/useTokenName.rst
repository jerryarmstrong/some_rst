packages/common/src/hooks/useTokenName.ts
=========================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useConnectionConfig } from '../contexts/connection';
import { getTokenName } from '../utils/utils';

export function useTokenName(mintAddress?: string | PublicKey) {
  const { tokenMap } = useConnectionConfig();
  const address =
    typeof mintAddress === 'string' ? mintAddress : mintAddress?.toBase58();
  return getTokenName(tokenMap, address);
}


