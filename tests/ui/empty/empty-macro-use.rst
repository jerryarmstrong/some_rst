tests/ui/empty/empty-macro-use.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

#[macro_use()]
extern crate two_macros;

pub fn main() {
    macro_two!();
    //~^ ERROR cannot find macro
}


