crates/credential/cargo-credential/README.md
============================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: md

    # cargo-credential

This package is a library to assist writing a Cargo credential helper, which
provides an interface to store tokens for authorizing access to a registry
such as https://crates.io/.

Documentation about credential processes may be found at
https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#credential-process

Example implementations may be found at
https://github.com/rust-lang/cargo/tree/master/crates/credential

## Usage

Create a Cargo project with this as a dependency:

```toml
# Add this to your Cargo.toml:

[dependencies]
cargo-credential = "0.1"
```

And then include a `main.rs` binary which implements the `Credential` trait, and calls
the `main` function which will call the appropriate method of the trait:

```rust
// src/main.rs

use cargo_credential::{Credential, Error};

struct MyCredential;

impl Credential for MyCredential {
    /// implement trait methods here...
}

fn main() {
    cargo_credential::main(MyCredential);
}
```


