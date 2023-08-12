src/tools/rustfmt/tests/source/configs/chain_width/tiny.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-chain_width: 20

struct Fluent {}

impl Fluent {
    fn blorp(&self) -> &Self {
        self
    }
}

fn main() {
    let test = Fluent {};

    // should not be wrapped
    test.blorp();
    test.blorp().blorp();

    // should be wrapped
    test.blorp().blorp().blorp();
    test.blorp().blorp().blorp().blorp();
}


