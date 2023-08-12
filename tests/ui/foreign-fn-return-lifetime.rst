tests/ui/foreign-fn-return-lifetime.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

extern "C" {
    pub fn g(_: &u8) -> &u8; // OK
    pub fn f() -> &u8; //~ ERROR missing lifetime specifier
}

fn main() {}


