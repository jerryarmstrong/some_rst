components/Members/types.ts
===========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { TokenOwnerRecord, VoteRecord } from '@solana/spl-governance'
import { ProgramAccount } from '@solana/spl-governance'

export enum ViewState {
  MainView,
  MemberOverview,
  AddMember,
}

export interface TokenRecordsWithWalletAddress {
  walletAddress: string
  council?: ProgramAccount<TokenOwnerRecord> | undefined
  community?: ProgramAccount<TokenOwnerRecord> | undefined
}

export interface WalletTokenRecordWithProposal
  extends ProgramAccount<VoteRecord> {
  proposalPublicKey: string
  proposalName: string
  chatMessages: string[]
}


