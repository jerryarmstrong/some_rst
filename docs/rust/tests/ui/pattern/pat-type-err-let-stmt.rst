tests/ui/pattern/pat-type-err-let-stmt.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test the `.span_label` to the type / scrutinee
// when there's a type error in checking a pattern.

fn main() {
    // We want to point at the `Option<u8>`.
    let Ok(0): Option<u8> = 42u8;
    //~^ ERROR mismatched types
    //~| ERROR mismatched types

    // We want to point at the `Option<u8>`.
    let Ok(0): Option<u8>;
    //~^ ERROR mismatched types

    // We want to point at the scrutinee.
    let Ok(0) = 42u8; //~ ERROR mismatched types
}


