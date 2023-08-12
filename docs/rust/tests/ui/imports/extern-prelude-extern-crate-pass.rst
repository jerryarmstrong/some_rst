tests/ui/imports/extern-prelude-extern-crate-pass.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:two_macros.rs

extern crate two_macros;

mod m {
    fn check() {
        two_macros::m!(); // OK
    }
}

fn main() {}


