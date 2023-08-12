js/packages/common/src/hooks/useTokenName.ts
============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useConnectionConfig } from '../contexts/connection';
import { getTokenName } from '../utils/utils';

export function useTokenName(mintAddress?: string | PublicKey) {
  const { tokens } = useConnectionConfig();
  const address =
    typeof mintAddress === 'string' ? mintAddress : mintAddress?.toBase58();
  return getTokenName(tokens, address);
}


