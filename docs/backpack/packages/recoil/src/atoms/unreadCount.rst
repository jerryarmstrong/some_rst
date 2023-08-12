packages/recoil/src/atoms/unreadCount.tsx
=========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { atom, selector } from "recoil";

export const unreadCount = atom<number>({
  key: "unreadCount",
  default: selector({
    key: "unreadCountDefaults",
    get: () => {
      return 0;
    },
  }),
});


