app/popup/types.ts
==================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { AccountInfo, PublicKey } from "@solana/web3.js"
import { Token } from "../core/types"

export type BalanceInfo = {
  amount: bigint
  lamports: bigint
  owner: PublicKey
  token: Token
}

export type OwnedAccount<T> = {
  publicKey: PublicKey
  accountInfo: AccountInfo<T>
}

export type MnemonicAndSeed = {
  mnemonic: string
  seed: string
}


