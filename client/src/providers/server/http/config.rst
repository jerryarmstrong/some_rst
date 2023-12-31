client/src/providers/server/http/config.ts
==========================================

Last edited: 2022-06-08 08:09:30

Contents:

.. code-block:: ts

    import { PublicKey, Cluster } from "@solana/web3.js";

export interface Config {
  cluster: Cluster | undefined;
  rpcUrl: string;
  programId: PublicKey;
  airdropEnabled: boolean;
}

function stringToCluster(str: string | undefined): Cluster | undefined {
  switch (str) {
    case "devnet":
    case "testnet":
    case "mainnet-beta": {
      return str;
    }
    default:
      return undefined;
  }
}

export function configFromInit(response: any): Config {
  const cluster = stringToCluster(response.cluster);
  return {
    cluster,
    rpcUrl: response.clusterUrl,
    programId: new PublicKey(response.programId),
    airdropEnabled: !response.paymentRequired,
  };
}


