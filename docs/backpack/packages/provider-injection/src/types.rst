packages/provider-injection/src/types.ts
========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export type WalletProvider = {
  on: (
    eventName: string | symbol,
    listener: (...args: unknown[]) => void
  ) => unknown;
  removeListener: (
    eventName: string | symbol,
    listener: (...args: unknown[]) => void
  ) => unknown;
  [optionalProps: string]: unknown;
};

type BackpackProvider = WalletProvider & {
  isBackpack: true;
};

export type WindowEthereum = WalletProvider & {
  isMetaMask?: boolean;
  isBackpack?: boolean;
  autoRefreshOnNetworkChange?: boolean;
};

interface Window {
  walletRouter?: {
    currentProvider: WalletProvider;
    providers: WalletProvider[];
    getProviderInfo: (
      provider: WalletProvider
    ) => WalletProvider["providerInfo"];
    addProvider: (newProvider: WalletProvider) => void;
  };
  ethereum?: WindowEthereum;
}


