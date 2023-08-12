README.md
=========

Last edited: 2021-02-03 12:40:10

Contents:

.. code-block:: md

    <p align="center">
  <a href="https://www.rosetta-api.org">
    <img width="90%" alt="Rosetta" src="https://www.rosetta-api.org/img/rosetta_header.png">
  </a>
</p>

<h3 align="center">
   Rosetta Solana
</h3>

<p align="center"><b>
ROSETTA-SOLANA IS CONSIDERED <a href="https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha">ALPHA SOFTWARE</a>.
USE AT YOUR OWN RISK!
</b></p>

## Overview
`rosetta-solana` provides a reference implementation of the Rosetta API for
Solana in Rust. If you haven't heard of the Rosetta API, you can find more
information [here](https://rosetta-api.org).

## Features
* Rosetta API implementation (both Data API and Construction API)
* Stateless, offline, curve-based transaction construction
* Simpler alternative Operations structure using metadata
* Supports most system and spl instructions

## Usage
As specified in the [Rosetta API Principles](https://www.rosetta-api.org/docs/automated_deployment.html),
all Rosetta implementations must be deployable via Docker and support running via either an
[`online` or `offline` mode](https://www.rosetta-api.org/docs/node_deployment.html#multiple-modes).

### Docker Install
Running the following commands will create a Docker image called `rosetta-solana:latest`.

##### From Source
After cloning this repository, run:
```text
docker build -t rosetta-solana .
docker-compose up
```

### Direct Install
After cloning this repository, run:
```text
cargo run build --release
```

## Testing with rosetta-cli
To validate `rosetta-solana`, [install `rosetta-cli`](https://github.com/coinbase/rosetta-cli#install)
and run one of the following commands:
* `rosetta-cli check:data --configuration-file rosetta-cli-conf/devnet.json`
* `rosetta-cli check:construction --configuration-file rosetta-cli-conf/devnet.json`

Note: If cli test gives EOF error it's probably due to golang trying to reuse connection and server closing it. I have disabled keep-alive for that reason. It's recommended to run cli test in dev mode.

## Development
* `cargo run` to run server
* `cargo run test` to run tests
* `cargo docs` to create docs

## Details

### Endpoints Implemented

```
    /network/list (network_list)
    /network/options (network_options)
    /network/status (network_status)
    /account/balance (account_balance)
    /block (get_block)
    /block/transaction (block_transaction)
    /call (call)
    /construction/combine (construction_combine)
    /construction/derive (construction_derive)
    /construction/hash (construction_hash)
    /construction/metadata (construction_metadata)
    /construction/parse (construction_parse)
    /construction/payloads (construction_payloads)
    /construction/preprocess (construction_preprocess)
    /construction/submit (construction_submit)
    
```
#### Default environment variables
```
RPC_URL = "https://devnet.solana.com"
NETWORK_NAME = "devnet"
HOST = "127.0.0.1"
PORT = "8080"
MODE = "online" //online/offline
```

#### Operations supported
See `types::OperationType` to see full list of current operations supported . This list might not be up to date.

```
 
    System__CreateAccount,
    System__Assign,
    System__Transfer,
    System__CreateNonceAccount,
    System__AdvanceNonce,
    System__WithdrawFromNonce,
    System__AuthorizeNonce,
    System__Allocate,
    SplToken__InitializeMint,
    SplToken__InitializeAccount,
    SplToken__CreateToken,
    SplToken__CreateAccount,
    SplToken__Transfer,
    SplToken__Approve,
    SplToken__Revoke,
    SplToken__MintTo,
    SplToken__Burn,
    SplToken__CloseAccount,
    SplToken__FreezeAccount,
    SplToken__ThawAccount,
    SplToken__TransferChecked,
    SplToken__CreateAssocAccount,

    Stake__CreateAccount,
    Stake__Delegate,
    Stake__Split,
    Stake__Merge,
    Stake__Authorize,
    Stake__Withdraw,
    Stake__Deactivate,
    Stake__SetLockup,

    Vote__CreateAccount,
    Vote__Authorize,
    Vote__Withdraw,
    Vote__UpdateValidatorIdentity,
    Vote__UpdateCommission,
    Unknown,
```

#### Simpler Operations

This implementation also supports writing operations using metadata only. Instead of writing two operations for a simple transfer transaction one can simply write a single operation and fill it's metadata e.g `source`, `destination`, `authority`, `lamports`. 

e.g 
```
[
    Operation{
        account: {address: "Sender"},
        amount: { value: "-10",...},
        ...
    },
    Operation{
        account: {address: "Receiver"},
        amount: {value: "10",...},
        ...
    }
]
```
```
[
    Operation{
        metadata: {
            source: "Sender",
            destination: "Receiver",
            lamports: 10
        },
        ...
    },
]
```
Both are same operations although the first one (Rosetta spec) always overwrites the second one.

#### Nonce transfers

To send a transaction with a nonce you need to add metadata to construction_preprosess with `{"metadata": {"with_nonce": {"account": "address of nonce account"}}}`

#### Balance changing Operations

See imp of `OperationType` in `src/types.rs` for list of balance changing operations. They might also require additional metadata depending on operation. Operation where only change is fees are not considered balance changing operation. Operation with only 1 balance change with no equal opposite signed opration are also not balance changing e.g mint or burn.


### Examples 
See tests in `src/construction.rs` to see complete working examples.

## TODO

* Add optional commitment option to every operation that accepts
* All preprocess metadata fetching for every operation type
* Suport all operation types
* Better errors
* Separate crates for proper docs

## License
This project is available open source under the terms of the [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0).


