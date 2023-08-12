packages/recoil/src/hooks/useUnreadCount.tsx
============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilState } from "recoil";

import * as atoms from "../atoms";

export const useUnreadCount = () => {
  return useRecoilState(atoms.unreadCount);
};


