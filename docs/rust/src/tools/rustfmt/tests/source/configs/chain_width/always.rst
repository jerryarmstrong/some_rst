src/tools/rustfmt/tests/source/configs/chain_width/always.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-chain_width: 1
// setting an unachievable chain_width to always get chains
// on separate lines

struct Fluent {}

impl Fluent {
    fn blorp(&self) -> &Self {
        self
    }
}

fn main() {
    let test = Fluent {};

    // should be left alone
    test.blorp();

    // should be wrapped
    test.blorp().blorp();
    test.blorp().blorp().blorp();
    test.blorp().blorp().blorp().blorp();
}


