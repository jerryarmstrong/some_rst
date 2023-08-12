packages/recoil/src/hooks/useUserMetadataMap.tsx
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilValue } from "recoil";

import { remoteUsersMetadataSelector } from "../atoms";

export function useUserMetadataMap({
  remoteUserIds,
  uuid,
}: {
  remoteUserIds: string[];
  uuid: string;
}) {
  return useRecoilValue(remoteUsersMetadataSelector({ remoteUserIds, uuid }));
}


