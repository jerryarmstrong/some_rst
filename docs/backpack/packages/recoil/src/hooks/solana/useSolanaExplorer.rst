packages/recoil/src/hooks/solana/useSolanaExplorer.tsx
======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../../atoms";

export function useSolanaExplorer(): string {
  return useRecoilValue(atoms.solanaExplorer)!;
}


