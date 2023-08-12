packages/recoil/src/hooks/solana/useJupiter.tsx
===============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { TokenInfo } from "@solana/spl-token-registry";
import { useRecoilValue } from "recoil";

import * as atoms from "../../atoms";
import type { TokenData } from "../../types";

export function useJupiterTokenList(): Array<TokenInfo> {
  return useRecoilValue(atoms.jupiterTokenList);
}

export function useJupiterTokenMap(): Map<string, TokenInfo> {
  return useRecoilValue(atoms.jupiterTokenMap);
}

export function useJupiterOutputTokens(inputMint: string): Array<TokenData> {
  return useRecoilValue(atoms.jupiterOutputTokens({ inputMint }));
}


