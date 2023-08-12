tests/ui/const-generics/const-argument-cross-crate-mismatch.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:const_generic_lib.rs

extern crate const_generic_lib;

fn main() {
    let _ = const_generic_lib::function(const_generic_lib::Struct([0u8, 1u8]));
    //~^ ERROR mismatched types
    let _: const_generic_lib::Alias = const_generic_lib::Struct([0u8, 1u8, 2u8]);
    //~^ ERROR mismatched types
}


