Strategies/components/psyfi/pdas.ts
===================================

Last edited: 2023-08-11 18:13:34

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


