tests/ui/consts/const-external-macro-const-err.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-build:external_macro.rs

// Ensure that CONST_ERR lint errors
// are not silenced in external macros.
// https://github.com/rust-lang/rust/issues/65300

extern crate external_macro;
use external_macro::static_assert;

fn main() {
    static_assert!(2 + 2 == 5); //~ ERROR constant
}


