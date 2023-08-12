clients/js/src/createTree.ts
============================

Last edited: 2023-08-12 00:00:44

Contents:

.. code-block:: ts

    /* eslint-disable no-bitwise */
import { createAccount } from '@metaplex-foundation/mpl-toolbox';
import {
  Context,
  Signer,
  TransactionBuilder,
  transactionBuilder,
} from '@metaplex-foundation/umi';
import {
  SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
  createTreeConfig,
} from './generated';
import { getMerkleTreeSize } from './hooked';

export const createTree = async (
  context: Parameters<typeof createAccount>[0] &
    Parameters<typeof createTreeConfig>[0] &
    Pick<Context, 'rpc'>,
  input: Omit<Parameters<typeof createTreeConfig>[1], 'merkleTree'> & {
    merkleTree: Signer;
    merkleTreeSize?: number;
    canopyDepth?: number;
  }
): Promise<TransactionBuilder> => {
  const space =
    input.merkleTreeSize ??
    getMerkleTreeSize(input.maxDepth, input.maxBufferSize, input.canopyDepth);
  const lamports = await context.rpc.getRent(space);

  return (
    transactionBuilder()
      // Create the empty Merkle tree account.
      .add(
        createAccount(context, {
          payer: input.payer ?? context.payer,
          newAccount: input.merkleTree,
          lamports,
          space,
          programId: context.programs.getPublicKey(
            'splAccountCompression',
            SPL_ACCOUNT_COMPRESSION_PROGRAM_ID
          ),
        })
      )
      // Create the tree config.
      .add(
        createTreeConfig(context, {
          ...input,
          merkleTree: input.merkleTree.publicKey,
        })
      )
  );
};


