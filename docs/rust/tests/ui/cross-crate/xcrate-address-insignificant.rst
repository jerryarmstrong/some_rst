tests/ui/cross-crate/xcrate-address-insignificant.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:xcrate_address_insignificant.rs


extern crate xcrate_address_insignificant as foo;

pub fn main() {
    assert_eq!(foo::foo::<f64>(), foo::bar());
}


