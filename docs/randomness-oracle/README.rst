README.md
=========

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: md

    # Randomness Oracle on Solana

Here you can find [random oracle program](./program/) and [off-chain broadcaster](./broadcaster) which pushes random value to the program account.

Random oracle program is simple program with literally two instructions `InitRandomnessOracle` and `UpdateRandomnessOracle`.

So from names it's clear that at first we init random oracle means create new account to hold random value. Random value is array `[u8; 32]`. The detailed info about values which are stored in random oracle account you can find [here](./program/src/state).

The second one instruction which is `UpdateRandomnessOracle` updates that value, it's permissioned instruction so only authority can broadcast new value.

As was mentioned above we also have [off-chain broadcaster](./broadcaster). It's Rust crate which should be launched preferably on cloud server. The role of that broadcaster is every new block generate random value and push it to the random oracle program. Generating random values is happening with help of [this crate](https://crates.io/crates/rand).

Also you can see in [example](./examples/eggs) how it can be used by other Solana program.

## Steps to run it

1. Build and deploy [random oracle program](./program/) with commands `cargo build-bpf` and `solana deploy`
2. Update program key in [`lib.rs` file](./program/src)
3. Run [off-chain broadcaster](./broadcaster) with command `cargo run start --owner 'path/to/keypair.json'`

