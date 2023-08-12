utils/uiTypes/members.ts
========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { BN } from '@coral-xyz/anchor'
import { PublicKey } from '@solana/web3.js'

export interface Member {
  walletAddress: string
  councilVotes: BN
  communityVotes: BN
  hasCouncilTokenOutsideRealm?: boolean
  hasCommunityTokenOutsideRealm?: boolean
  delegateWalletCouncil?: PublicKey
  delegateWalletCommunity?: PublicKey
}

interface Delegate {
  communityMembers?: Array<Member>
  councilMembers?: Array<Member>
  communityTokenCount?: BN
  councilTokenCount?: BN
}

export interface Delegates {
  [key: string]: Delegate
}


