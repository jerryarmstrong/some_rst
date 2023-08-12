tests/ui/suggestions/mismatched-types-numeric-from.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: u32 = i32::from(0_u8); //~ ERROR mismatched types
}


