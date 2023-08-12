packages/use-solana/src/utils/useProviderInternal.ts
====================================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import type {
  AugmentedProvider,
  ReadonlyProvider,
} from "@saberhq/solana-contrib";
import {
  DEFAULT_PROVIDER_OPTIONS,
  SolanaAugmentedProvider,
  SolanaReadonlyProvider,
} from "@saberhq/solana-contrib";
import type { Commitment, ConfirmOptions, Connection } from "@solana/web3.js";
import { useMemo } from "react";

import type { ConnectedWallet, WalletAdapter } from "../adapters/types";
import { WalletAdapterProvider } from "./provider";

/**
 * Wallet-related information.
 */
export interface UseProvider {
  /**
   * Read-only provider.
   */
  provider: ReadonlyProvider;
  /**
   * {@link Provider} of the currently connected wallet.
   */
  providerMut: AugmentedProvider | null;
}

export interface UseProviderArgs {
  /**
   * Connection.
   */
  connection: Connection;
  /**
   * Send connection.
   */
  sendConnection?: Connection;
  /**
   * Broadcast connections.
   */
  broadcastConnections?: Connection[];
  /**
   * Wallet.
   */
  wallet?: WalletAdapter<boolean>;
  /**
   * Commitment for the read-only provider.
   */
  commitment?: Commitment;
  /**
   * Confirm options for the mutable provider.
   */
  confirmOptions?: ConfirmOptions;
}

export const useProviderInternal = ({
  connection,
  sendConnection = connection,
  broadcastConnections = [sendConnection],
  wallet,
  commitment = "confirmed",
  confirmOptions = DEFAULT_PROVIDER_OPTIONS,
}: UseProviderArgs): UseProvider => {
  const provider = useMemo(
    () =>
      new SolanaReadonlyProvider(connection, {
        commitment,
      }),
    [commitment, connection]
  );

  const connected = wallet?.connected;
  const publicKey = wallet?.publicKey;
  const providerMut = useMemo(
    () =>
      wallet && connected && publicKey
        ? new SolanaAugmentedProvider(
            WalletAdapterProvider.init({
              connection,
              broadcastConnections,
              wallet: wallet as ConnectedWallet,
              opts: confirmOptions,
            })
          )
        : null,
    [
      wallet,
      connected,
      publicKey,
      connection,
      broadcastConnections,
      confirmOptions,
    ]
  );

  return {
    provider,
    providerMut,
  };
};


