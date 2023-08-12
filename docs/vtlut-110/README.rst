README.md
=========

Last edited: 2022-10-31 20:56:14

Contents:

.. code-block:: md

    ## Versioned Transactions and Address Lookup Tables on Solana 1.10

Versioned Transactions and Address Lookup Tables are only fully supported on Solana 1.13+. A large number of Solana 
programs are stuck on Solana 1.10 due to dependence on Anchor 0.25 which pins to Solana 1.10 patch versions. This crate
implements the required types, and some convenience methods, necessary to create Versioned Transactions and use Address Lookup Tables while remaining locked
to Solana 1.10. It also contains instructions for the Solana Address Lookup Table Program to allow Rust clients to 
use this table without importing Solana 1.14. 

### Example Usage

Create the VersionedMessageArgs struct or a custom `Vm` type:

```rust
    let vm = VersionedMessageArgs {
        payer,
        instructions,
        address_luts: vec![address_lookup_table_account],
        latest_blockhash,
    };
```

Pass this in to the `Vt::new()` method and then call `sign_and_send` with a reference to the Solana client.

```rust
    let vt = Vt::new(vm, vec![payer_kp, nft_mint])?;

    let signature = vt.sign_and_send(&program.rpc())?;
```



