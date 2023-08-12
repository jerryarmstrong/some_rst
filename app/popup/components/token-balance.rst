app/popup/components/token-balance.tsx
======================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import { PublicKey } from "@solana/web3.js"
import { LoadingIndicator } from "./loading-indicator"
import { BalanceInfo } from "../types"
import { formatAddress, formatAmount } from "../utils/format"

interface TokenBalanceProp {
  publicKey: PublicKey
  balanceInfo: BalanceInfo
}

export const TokenBalance: React.FC<TokenBalanceProp> = ({ publicKey, balanceInfo }) => {
  let { amount, token } = balanceInfo
  return (
    <div>
      {formatAmount(amount, token.decimals)}{" "}
      {token.symbol !== "" ? token.symbol : token.mintAddress && formatAddress(token.mintAddress)}
    </div>
  )
}


