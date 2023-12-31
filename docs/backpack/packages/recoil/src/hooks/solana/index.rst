packages/recoil/src/hooks/solana/index.tsx
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { RawMintWithProgramIdString } from "@coral-xyz/common";
import { useRecoilValue } from "recoil";

import * as atoms from "../../atoms";

export * from "./recentTransactionHelpers";
export * from "./useJupiter";
export * from "./useLoadSplTokens";
export * from "./usePlugins";
export * from "./useRecentTransactions";
export * from "./useSolanaCommitment";
export * from "./useSolanaConnection";
export * from "./useSolanaExplorer";
export * from "./useSolanaTransaction";
export * from "./useSplTokenRegistry";

export function useSolanaTokenMint({
  publicKey,
  tokenAddress,
}: {
  publicKey: string;
  tokenAddress: string;
}): RawMintWithProgramIdString {
  return useRecoilValue(atoms.solanaTokenMint({ tokenAddress, publicKey }));
}


