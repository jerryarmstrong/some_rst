tests/ui/imports/extern-prelude-extern-crate-cfg.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// compile-flags:--cfg my_feature

#![no_std]

#[cfg(my_feature)]
extern crate std;

mod m {
    #[cfg(my_feature)]
    fn conditional() {
        std::vec::Vec::<u8>::new(); // OK
    }
}

fn main() {}


