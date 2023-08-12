packages/chat-xplat/src/utils/refreshGroupsAndFriendships.tsx
=============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { refreshFriendships, refreshGroups } from "@coral-xyz/db";

import { SignalingManager } from "./SignalingManager";

export const refreshGroupsAndFriendships = async (
  uuid: string,
  jwt?: string
) => {
  try {
    await Promise.all([
      refreshFriendships(uuid, jwt),
      refreshGroups(uuid, jwt),
    ]);
  } catch (e) {
    console.error("Error while refreshing friendships and groups");
    console.error(e);
  }
  SignalingManager.getInstance().onUpdateRecoil({
    type: "friendship",
  });
  SignalingManager.getInstance().onUpdateRecoil({
    type: "collection",
  });
};


