packages/recoil/src/hooks/useXnftPreferences.tsx
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export const useXnftPreferences = () => {
  return useRecoilValue(atoms.xnftPreferences);
};

export function useXnftPreference(xnftId?: string) {
  if (!xnftId) {
    return null;
  }
  return useRecoilValue(atoms.xnftPreference(xnftId));
}


