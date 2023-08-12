packages/recoil/src/atoms/avatar.ts
===================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { atomFamily } from "recoil";

type NewAvatar = {
  url: string;
  id: string;
};
type Username = string;
/**
 * Store updated Avatar data
 */
export const newAvatarAtom = atomFamily<NewAvatar | null, Username>({
  key: "newAvatarAtom",
  default: null,
});


