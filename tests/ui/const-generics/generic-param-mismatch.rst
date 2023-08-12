tests/ui/const-generics/generic-param-mismatch.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test<const N: usize, const M: usize>() -> [u8; M] {
    [0; N] //~ ERROR mismatched types
}

fn main() {}


