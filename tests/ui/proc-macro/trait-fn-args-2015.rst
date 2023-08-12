tests/ui/proc-macro/trait-fn-args-2015.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Unnamed arguments in trait functions can be passed through proc macros on 2015 edition.

// check-pass
// aux-build:test-macros.rs

#![allow(anonymous_parameters)]

#[macro_use]
extern crate test_macros;

trait Tr {
    #[identity_attr]
    fn method(u8);
}

fn main() {}


