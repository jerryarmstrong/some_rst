token-vault/js/src/instructions/mint-shares-to-treasury.ts
==========================================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { bignum } from '@metaplex-foundation/beet';
import {
  createMintFractionalSharesInstruction,
  MintFractionalSharesInstructionAccounts,
  MintFractionalSharesInstructionArgs,
} from '../generated';

/**
 * Mints shares to the {@link MintFractionalSharesInstructionAccounts.fractionTreasury}.
 *
 * ### Conditions for {@link MintFractionalSharesInstructionAccounts} accounts to add token to vault
 *
 * _Aside from the conditions outlined in detail in {@link InitVault.initVault}_ the following should hold:
 *
 * #### vault
 *
 * - state: {@link VaultState.Active}
 * - allowFurtherShareCreation: true
 *
 * #### fractionTreasury
 *
 * - address: vault.fractionTreasury
 *
 * #### fractionMint
 *
 * - adddress: vault.fractionMint
 *
 * ### Updates as a result of completing the Transaction
 *
 * #### fractionTreasury
 *
 * - amount: increased by {@link numberOfShares}
 */
export function mintSharesToTreasury(
  accounts: MintFractionalSharesInstructionAccounts,
  numberOfShares: bignum,
) {
  const args: MintFractionalSharesInstructionArgs = { numberOfShareArgs: { numberOfShares } };

  return createMintFractionalSharesInstruction(accounts, args);
}


