js/packages/common/src/hooks/useAccountByMint.ts
================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useUserAccounts } from '../hooks/useUserAccounts';

export const useAccountByMint = (mint?: string | PublicKey) => {
  const { userAccounts } = useUserAccounts();
  const mintAddress = typeof mint === 'string' ? mint : mint?.toBase58();

  const index = userAccounts.findIndex(
    acc => acc.info.mint.toBase58() === mintAddress,
  );

  if (index !== -1) {
    return userAccounts[index];
  }

  return;
};


