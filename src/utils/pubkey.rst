src/utils/pubkey.ts
===================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'
import { strict as assert } from 'assert'

/**
 * Checks if a string is valid base58 Solana via a Regex.
 * @private
 */
export function isValidSolanaAddress(address: string) {
  return /^[0-9a-zA-Z]{43,88}$/.test(address)
}

export function assertValidSolanaAddress(address: string) {
  assert(
    isValidSolanaAddress(address) && address.length >= 44,
    `'${address}' is not a valid solana account or transaction address`
  )
}

/**
 * Checks if a string is valid PublicKey address.
 * @private
 */
export function isValidPublicKeyAddress(address: string) {
  if (!isValidSolanaAddress(address) || address.length > 44) return false
  try {
    new PublicKey(address)
    return true
  } catch (_) {
    return false
  }
}

export function asPublicKey(address: string): PublicKey {
  assertValidSolanaAddress(address)
  return new PublicKey(address)
}


