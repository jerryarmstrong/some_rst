tests/ui/array-slice-vec/match_arr_unknown_len.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn is_123<const N: usize>(x: [u32; N]) -> bool {
    match x {
        [1, 2] => true, //~ ERROR mismatched types
        _ => false
    }
}

fn main() {}


