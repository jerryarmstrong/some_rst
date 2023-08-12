packages/token-utils/src/index.ts
=================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    /**
 * [[include:token-utils/README.md]]
 * @module
 */

export * from "./ata.js";
export * from "./instructions/index.js";
export * from "./layout.js";
export * from "./price.js";
export * from "./splTokenRegistry.js";
export * from "./token.js";
export * from "./tokenAmount.js";
export * from "./tokenList.js";
export * from "./tokenOwner.js";
export * from "./tokenProvider.js";

// re-export token-math types
// so consumers don't need to use them

export type { BigintIsh, IFormatUint, NumberFormat } from "@ubeswap/token-math";
export {
  Fraction,
  makeDecimalMultiplier,
  MAX_U64,
  MAX_U256,
  ONE,
  parseBigintIsh,
  Percent,
  Rounding,
  TEN,
  validateU64,
  validateU256,
  ZERO,
} from "@ubeswap/token-math";

// serum common
export * from "./common.js";

// re-export SPL token types
export type {
  AuthorityType,
  Mint as MintData,
  Multisig,
} from "@solana/spl-token";
export {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  NATIVE_MINT,
  TOKEN_PROGRAM_ID,
} from "@solana/spl-token";
export { u64 } from "@solana/buffer-layout-utils";


