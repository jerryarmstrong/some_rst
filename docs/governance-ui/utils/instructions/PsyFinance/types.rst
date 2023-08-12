utils/instructions/PsyFinance/types.ts
======================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import * as anchor from '@coral-xyz/anchor'
import { PublicKey } from '@solana/web3.js'

export type OptionMarket = {
  optionMint: PublicKey
  writerTokenMint: PublicKey
  underlyingAssetMint: PublicKey
  quoteAssetMint: PublicKey
  underlyingAssetPool: PublicKey
  quoteAssetPool: PublicKey
  mintFeeAccount: PublicKey
  exerciseFeeAccount: PublicKey
  underlyingAmountPerContract: anchor.BN
  quoteAmountPerContract: anchor.BN
  expirationUnixTimestamp: anchor.BN
  expired: boolean
  bumpSeed: number
}

export type OptionMarketWithKey = OptionMarket & {
  key: PublicKey
}


