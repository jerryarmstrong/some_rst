packages/recoil/src/atoms/primaryWallets.tsx
============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { ServerPublicKey } from "@coral-xyz/common";
import { selector } from "recoil";

import { serverPublicKeys } from "./wallet";

export const primaryWallets = selector<Array<ServerPublicKey>>({
  key: "primaryWallets",
  get: ({ get }) => {
    return get(serverPublicKeys).filter((s) => s.primary);
  },
});


