packages/recoil/src/hooks/useRecentNotifications.tsx
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export const useRecentNotifications = ({
  limit,
  offset,
  uuid,
}: {
  limit: number;
  offset: number;
  uuid: string;
}) => {
  return useRecoilValue(atoms.recentNotifications({ limit, offset, uuid }));
};


