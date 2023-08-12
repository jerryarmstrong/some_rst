utils/uiTypes/NftVoterClient.ts
===============================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { Program, Provider } from '@project-serum/anchor'
import { PublicKey } from '@solana/web3.js'
import { NftVoter, IDL } from '../../idls/nft_voter'
import { DEFAULT_NFT_VOTER_PLUGIN } from '@tools/constants'

export class NftVoterClient {
  constructor(public program: Program<NftVoter>, public devnet?: boolean) {}

  static connect(
    provider: Provider,
    devnet?: boolean,
    programId = new PublicKey(DEFAULT_NFT_VOTER_PLUGIN)
  ): NftVoterClient {
    return new NftVoterClient(
      new Program<NftVoter>(IDL, programId, provider),
      devnet
    )
  }
}


