tests/ui/issues/auxiliary/cgu_test_a.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: -Ccodegen-units=2 --crate-type=lib

extern crate cgu_test;

pub mod a {
    pub fn a() {
        ::cgu_test::id(0);
    }
}
pub mod b {
    pub fn a() {
        ::cgu_test::id(0);
    }
}


