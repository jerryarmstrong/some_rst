packages/recoil/src/hooks/useFeatureGates.tsx
=============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export const useFeatureGates = () => {
  return useRecoilValue(atoms.featureGates);
};


