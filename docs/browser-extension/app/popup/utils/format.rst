app/popup/utils/format.ts
=========================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js"

const balanceFormat = new Intl.NumberFormat(undefined, {
  minimumFractionDigits: 4,
  maximumFractionDigits: 10,
  useGrouping: true,
})

export const formatSolAmount = (amount: number | bigint) => {
  return formatAmount(amount, 9)
}

export const formatAmount = (amount: number | bigint, decimals: number): string => {
  let stringAmount = ""
  if (typeof amount == "number") {
    stringAmount = "" + amount / Math.pow(10, decimals)
  } else {
    stringAmount =
      "" + amount / BigInt(Math.pow(10, decimals)) + "." + (amount % BigInt(Math.pow(10, decimals)))
  }
  return balanceFormat.format(parseFloat(stringAmount))
}

export function formatAddress(address: string) {
  return address.slice(0, 4) + "…" + address.slice(address.length - 4)
}


