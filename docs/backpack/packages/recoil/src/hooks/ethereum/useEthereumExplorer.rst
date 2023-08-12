packages/recoil/src/hooks/ethereum/useEthereumExplorer.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../../atoms";

export function useEthereumExplorer(): string {
  return useRecoilValue(atoms.ethereumExplorer)!;
}


