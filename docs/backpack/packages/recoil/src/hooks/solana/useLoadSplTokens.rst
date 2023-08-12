packages/recoil/src/hooks/solana/useLoadSplTokens.tsx
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { CustomSplTokenAccountsResponseString } from "@coral-xyz/common";
import { useRecoilCallback } from "recoil";

import * as atoms from "../../atoms";

export const useUpdateAllSplTokenAccounts = () =>
  useRecoilCallback(
    ({ set }: any) =>
      async ({
        connectionUrl,
        publicKey,
        customSplTokenAccounts,
      }: {
        connectionUrl: string;
        publicKey: string;
        customSplTokenAccounts: CustomSplTokenAccountsResponseString;
      }) => {
        // TODO: Do we want to check if the atoms have changed before setting
        //       them? Probably since we don't have a recoil transaction and
        //       so this hook may cause unnecessary rerenders.
        set(atoms.customSplTokenAccounts({ connectionUrl, publicKey }), {
          ...customSplTokenAccounts,
          splTokenMints: new Map(customSplTokenAccounts.mintsMap),
        });
      }
  );


