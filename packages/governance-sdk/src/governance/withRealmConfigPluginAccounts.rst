packages/governance-sdk/src/governance/withRealmConfigPluginAccounts.ts
=======================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { AccountMeta, PublicKey } from '@solana/web3.js';
import { getRealmConfigAddress } from './accounts';

export async function withRealmConfigPluginAccounts(
  keys: AccountMeta[],
  programId: PublicKey,
  realm: PublicKey,
  voterWeightRecord?: PublicKey | undefined,
  maxVoterWeightRecord?: PublicKey | undefined,
) {
  const realmConfigAddress = await getRealmConfigAddress(programId, realm);

  keys.push({
    pubkey: realmConfigAddress,
    isWritable: false,
    isSigner: false,
  });

  if (voterWeightRecord) {
    keys.push({
      pubkey: voterWeightRecord,
      isWritable: false,
      isSigner: false,
    });
  }

  if (maxVoterWeightRecord) {
    keys.push({
      pubkey: maxVoterWeightRecord,
      isWritable: false,
      isSigner: false,
    });
  }
}


