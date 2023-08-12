packages/governance/src/actions/createTreasuryAccount.ts
========================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Keypair, PublicKey, TransactionInstruction } from '@solana/web3.js';

import { GovernanceConfig } from '@solana/spl-governance';

import { sendTransactionWithNotifications } from '../tools/transactions';

import { withCreateTokenGovernance } from '@solana/spl-governance';
import { RpcContext } from '@solana/spl-governance';
import { withCreateSplTokenAccount } from '../tools/sdk/token/splToken';

export const createTreasuryAccount = async (
  { connection, wallet, programId, programVersion, walletPubkey }: RpcContext,
  realm: PublicKey,
  mint: PublicKey,
  config: GovernanceConfig,
  tokenOwnerRecord: PublicKey,
): Promise<PublicKey> => {
  let instructions: TransactionInstruction[] = [];
  let signers: Keypair[] = [];

  const tokenAccount = await withCreateSplTokenAccount(
    instructions,
    signers,
    connection,
    mint,
    walletPubkey,
    walletPubkey,
  );

  let governanceAddress;
  let governanceAuthority = walletPubkey;

  governanceAddress = await withCreateTokenGovernance(
    instructions,
    programId,
    programVersion,
    realm,
    tokenAccount,
    config,
    true,
    walletPubkey,
    tokenOwnerRecord,
    walletPubkey,
    governanceAuthority,
  );

  await sendTransactionWithNotifications(
    connection,
    wallet,
    instructions,
    signers,
    'Creating treasury account',
    'Treasury account has been created',
  );

  return governanceAddress;
};


