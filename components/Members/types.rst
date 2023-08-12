components/Members/types.ts
===========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { VoteRecord } from '@solana/spl-governance'
import { ProgramAccount } from '@solana/spl-governance'

export interface WalletTokenRecordWithProposal
  extends ProgramAccount<VoteRecord> {
  proposalPublicKey: string
  proposalName: string
  chatMessages: string[]
}


