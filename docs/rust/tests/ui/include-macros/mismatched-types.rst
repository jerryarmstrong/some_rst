tests/ui/include-macros/mismatched-types.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let b: &[u8] = include_str!("file.txt");    //~ ERROR mismatched types
    let s: &str = include_bytes!("file.txt");   //~ ERROR mismatched types
}


