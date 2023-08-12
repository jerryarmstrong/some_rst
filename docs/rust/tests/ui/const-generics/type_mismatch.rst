tests/ui/const-generics/type_mismatch.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<const N: usize>() -> [u8; N] {
    bar::<N>() //~ ERROR mismatched types
}

fn bar<const N: u8>() -> [u8; N] {}
//~^ ERROR mismatched types
//~| ERROR mismatched types

fn main() {}


