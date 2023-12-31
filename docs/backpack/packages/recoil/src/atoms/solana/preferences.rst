packages/recoil/src/atoms/solana/preferences.tsx
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { Commitment } from "@solana/web3.js";
import { selector } from "recoil";

import { preferences } from "../preferences";

export const solanaExplorer = selector<string>({
  key: "solanaExplorer",
  get: async ({ get }) => {
    const p = get(preferences);
    return p.solana.explorer;
  },
});

export const solanaCommitment = selector<Commitment>({
  key: "solanaCommitment",
  get: async ({ get }) => {
    const p = get(preferences);
    return p.solana.commitment;
  },
});

/**
 * URL to the cluster to communicate with.
 */
export const solanaConnectionUrl = selector<string>({
  key: "solanaConnectionUrl",
  get: ({ get }) => {
    const p = get(preferences);
    return p.solana.cluster;
  },
});

export const eclipseConnectionUrl = selector<string>({
  key: "eclipseConnectionUrl",
  get: ({ get }) => {
    const p = get(preferences);
    return p.eclipse.cluster;
  },
});


