tests/ui/invalid/invalid-crate-type-macro.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = foo!()] //~ ERROR malformed `crate_type` attribute

macro_rules! foo {
    () => {"rlib"};
}

fn main() {}


