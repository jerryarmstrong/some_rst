tests/ui/cross-crate/xcrate_generic_fn_nested_return.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:xcrate_generic_fn_nested_return.rs

extern crate xcrate_generic_fn_nested_return as test;

pub fn main() {
    assert!(test::decode::<()>().is_err());
}


