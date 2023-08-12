packages/recoil/src/hooks/useTotalBalance.tsx
=============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export function useTotalBalance(): any {
  return useRecoilValue(atoms.totalBalance);
}


