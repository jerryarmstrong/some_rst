README.md
=========

Last edited: 2020-05-08 23:31:17

Contents:

.. code-block:: md

    [![Build status][travis-image]][travis-url]

[travis-image]: https://travis-ci.org/solana-labs/example-tictactoe.svg?branch=v1.1
[travis-url]: https://travis-ci.org/solana-labs/example-tictactoe

# Tic-Tac-Toe on Solana

This project demonstrates how to use the [Solana Javascript API](https://github.com/solana-labs/solana-web3.js)
to build, deploy, and interact with programs on the Solana blockchain, implementing an interactive tic-tac-toe game between two users.
To see the final product, go to https://solana-example-tictactoe.herokuapp.com/ and wait for another player to join.
(Direct a second browser window to the web app to play against yourself.)

The project comprises:

* The on-chain Tic-Tac-Toe program, a BPF program written in Rust `program-bpf-rust` and C `program-bpf-c`
* Easy program build and deployment using the `@solana/web3.js` library
* Command-line and web front-end: `src/`

## Learn about Solana

More information about how Solana works is available in the [Book](https://docs.solana.com/book/)

## Getting Started

The following dependencies are required to build and run this example,
depending on your OS they may already be installed:

```sh
$ npm --version
$ docker -v
$ wget --version
$ rustc --version
```

Next fetch the npm dependencies, including `@solana/web3.js`, by running:
```sh
$ npm install
```

### Select a Network
The example connects to a local Solana cluster by default.

To enable on-chain program logs, set the `RUST_LOG` environment variable:
```sh
$ export RUST_LOG=solana_runtime::native_loader=trace,solana_runtime::system_instruction_processor=trace,solana_runtime::bank=debug,solana_bpf_loader=debug,solana_rbpf=debug
```

To start a local Solana cluster run:
```sh
$ npm run localnet:update
$ npm run localnet:up
```

Solana cluster logs are available with:
```sh
$ npm run localnet:logs
```

To stop the local solana cluster run:
```sh
$ npm run localnet:down
```

For more details on working with a local cluster, see the [full instructions](https://github.com/solana-labs/solana-web3.js#local-network).

### Build the BPF program
```sh
$ npm run build:bpf-rust
```
or
```
$ npm run build:bpf-c
```

The compiler places output files in `dist/program`. Program build scripts contain the compiler settings and can be found in the [Solana SDK](https://github.com/solana-labs/solana/tree/master/sdk/bpf/rust)

### Run the Command-Line Front End
After building the program,

```sh
$ npm run start
```

This script uses the Solana Javascript API `BpfLoader` to deploy the Tic-Tac-Toe program to the blockchain.
Once the deploy transaction is confirmed on the chain, the script calls the program to instantiate a new dashboard
to track the open and completed games (`findDashboard`), and starts a new game (`dashboard.startGame`), waiting for an opponent.

To play the game, open a second terminal and again run the `npm run start` script.

To see the program or game state on the blockchain, send a `getAccountInfo` [JSON-RPC request](https://solana-labs.github.io/solana/jsonrpc-api.html#getaccountinfo) to the cluster, using the id printed by the script, eg.:
* `Dashboard programId: HFA4x4oZKWeGcRVbUYaCHM59i5AFfP3nCfc4NkrBvVtP`
* `Dashboard: HmAEDrGpsRK2PkR51E9mQrKQG7Qa3iyv4SvZND9uEkdR`
* `Advertising our game (Gx1kjBieYgaPgDhaovzvvZapUTg5Mz6nhXTLWSQJpNMv)`

### Run the WebApp Front End
After building the program,

```sh
$ npm run dev
```

This script deploys the program to the blockchain and also boots up a local webserver
for gameplay.

To instantiate a dashboard and game, open your browser to [http://localhost:8080/](http://localhost:8080/).

## Customizing the Program
To customize Tic-Tac-Toe, make changes to the program in `program-bpf-rust/src`, rebuild it, and restart the network.
Now when you run `npm run start`, you should see your changes.

To deploy a program with a different name, edit `src/server/config.js`.

## Pointing to a public Solana cluster

Solana maintains three public clusters:
- `devnet` - Development cluster with airdrops enabled
- `testnet` - Tour De Sol test cluster without airdrops enabled
- `mainnet-beta` -  Main cluster
  
Use npm scripts to configure which cluster.

To point to `devnet`:
```bash
$ npm run cluster:devnet
```

To point back to the local cluster:
```bash
$ npm run cluster:localnet
```

