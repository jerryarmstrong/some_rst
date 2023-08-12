tests/ui/macros/macro-use-all-and-none.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:two_macros-rpass.rs

#![warn(unused_attributes)]

#[macro_use]
#[macro_use()] //~ WARNING unused attribute
extern crate two_macros_rpass;

pub fn main() {
    macro_one!();
    macro_two!();
}


