tests/ui/imports/extern-prelude-extern-crate-restricted-shadowing.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

macro_rules! define_vec {
    () => {
        extern crate std as Vec;
    }
}

define_vec!();

mod m {
    fn check() {
        Vec::panic!(); //~ ERROR `Vec` is ambiguous
    }
}

macro_rules! define_other_core {
    () => {
        extern crate std as core;
        //~^ ERROR macro-expanded `extern crate` items cannot shadow names passed with `--extern`
    }
}

define_other_core!();

fn main() {}


