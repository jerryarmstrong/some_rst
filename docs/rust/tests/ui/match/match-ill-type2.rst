tests/ui/match/match-ill-type2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 1i32 {
        1i32 => 1,
        2u32 => 1, //~ ERROR mismatched types
        _ => 2,
    };
}


