packages/app-mobile/src/lib/WalletUtils.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { Blockchain } from "@coral-xyz/common";
import type { Wallet } from "@coral-xyz/recoil";

import { formatUsd } from "@coral-xyz/common";

type WalletData = Wallet & {
  balance: string;
  isPrimary: boolean;
};

export function coalesceWalletData(
  graphqlData,
  recoilWallets: Wallet[]
): WalletData[] {
  return graphqlData.user.wallets.edges.map((edge) => {
    const a = recoilWallets.find(
      (wallet) => wallet.publicKey === edge.node.address
    );

    return {
      ...edge.node,
      // wallet name & type comes from recoil for the foreseeable future. Privacy concern
      name: a?.name ?? "",
      type: a?.type ?? "",
      isCold: a?.isCold ?? false,
      publicKey: edge.node.address,
      blockchain: edge.node.provider.name.toLowerCase() as Blockchain,
      isPrimary: edge.node.isPrimary,
      balance: formatUsd(edge.node.balances.aggregate.value),
    };
  });
}


