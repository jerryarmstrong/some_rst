packages/recoil/src/hooks/usePrimaryWallets.tsx
===============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export const usePrimaryWallets = () => {
  return useRecoilValue(atoms.primaryWallets);
};


