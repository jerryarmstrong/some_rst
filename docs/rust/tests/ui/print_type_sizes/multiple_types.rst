tests/ui/print_type_sizes/multiple_types.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes --crate-type=lib
// build-pass

// This file illustrates that when multiple structural types occur in
// a function, every one of them is included in the output.

pub struct SevenBytes([u8;  7]);
pub struct FiftyBytes([u8; 50]);

pub enum Enum {
    Small(SevenBytes),
    Large(FiftyBytes),
}


