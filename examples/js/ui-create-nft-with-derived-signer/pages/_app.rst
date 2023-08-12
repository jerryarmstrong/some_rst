examples/js/ui-create-nft-with-derived-signer/pages/_app.tsx
============================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: tsx

    import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import { WalletProvider } from "@solana/wallet-adapter-react";
import { WalletModalProvider } from "@solana/wallet-adapter-react-ui";
import {
  LedgerWalletAdapter,
  PhantomWalletAdapter,
  SolflareWalletAdapter,
} from "@solana/wallet-adapter-wallets";
import { clusterApiUrl } from "@solana/web3.js";
import type { AppProps } from "next/app";
import { useMemo } from "react";
import { UmiProvider } from "./UmiProvider";

import "@/styles/globals.css";
import "@solana/wallet-adapter-react-ui/styles.css";

export default function App({ Component, pageProps }: AppProps) {
  const network = WalletAdapterNetwork.Devnet;
  const endpoint = useMemo(() => clusterApiUrl(network), [network]);
  const wallets = useMemo(
    () => [
      new LedgerWalletAdapter(),
      new PhantomWalletAdapter(),
      new SolflareWalletAdapter({ network }),
    ],
    [network]
  );

  return (
    <WalletProvider wallets={wallets} autoConnect>
      <UmiProvider endpoint={endpoint}>
        <WalletModalProvider>
          <Component {...pageProps} />
        </WalletModalProvider>
      </UmiProvider>
    </WalletProvider>
  );
}


