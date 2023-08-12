Strategies/components/psyfi/pdas.ts
===================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'

export const deriveVaultCollateralAccount = async (
  programKey: PublicKey,
  vaultAccount: PublicKey
) => {
  return await PublicKey.findProgramAddress(
    [
      new PublicKey(vaultAccount).toBuffer(),
      Buffer.from('VaultCollateralAccount'),
    ],
    programKey
  )
}


