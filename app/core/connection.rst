app/core/connection.ts
======================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { Connection } from "@solana/web3.js"
import { createLogger } from "./utils"
import { Network } from "./types"

const log = createLogger("sol:conn")

export class Web3Connection {
  public conn: Connection
  public network: Network

  constructor(network: Network) {
    log("Initializing connection network: %O", network)
    this.network = network
    this.conn = new Connection(network.endpoint)
  }

  changeNetwork(network: Network) {
    log("Changing connection network: %O", network)
    this.network = network
    this.conn = new Connection(network.endpoint)
  }
}


