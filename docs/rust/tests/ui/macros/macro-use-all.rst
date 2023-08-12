tests/ui/macros/macro-use-all.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:two_macros.rs

#[macro_use]
extern crate two_macros;

pub fn main() {
    macro_one!();
    macro_two!();
}


