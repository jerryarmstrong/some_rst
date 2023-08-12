packages/recoil/src/hooks/ethereum/useUpdateEthereumBalances.tsx
================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilCallback } from "recoil";

import * as atoms from "../../atoms";

export const useUpdateEthereumBalances = () =>
  useRecoilCallback(
    ({ set }: any) =>
      async ({
        connectionUrl,
        publicKey,
        balances,
      }: {
        connectionUrl: string;
        publicKey: string;
        balances: any;
      }) => {
        set(
          atoms.ethereumBalances({
            connectionUrl,
            publicKey,
          }),
          new Map(Object.entries(balances))
        );
      }
  );


