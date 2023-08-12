packages/recoil/src/hooks/solana/useSolanaCommitment.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { Commitment } from "@solana/web3.js";
import { useRecoilValue } from "recoil";

import * as atoms from "../../atoms";

export function useSolanaCommitment(): Commitment {
  return useRecoilValue(atoms.solanaCommitment)!;
}


