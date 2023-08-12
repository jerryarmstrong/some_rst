tests/ui/macros/macro-use-undef.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

#[macro_use(macro_two, no_way)] //~ ERROR imported macro not found
extern crate two_macros;

pub fn main() {
    macro_two!();
}


