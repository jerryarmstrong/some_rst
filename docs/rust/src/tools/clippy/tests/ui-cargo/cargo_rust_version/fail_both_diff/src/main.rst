src/tools/clippy/tests/ui-cargo/cargo_rust_version/fail_both_diff/src/main.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::use_self)]

pub struct Foo;

impl Foo {
    pub fn bar() -> Foo {
        Foo
    }
}

fn main() {}


