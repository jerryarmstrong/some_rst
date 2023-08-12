tests/ui/str/str-lit-type-mismatch.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &[u8] = "foo"; //~ ERROR mismatched types
    let y: &[u8; 4] = "baaa"; //~ ERROR mismatched types
    let z: &str = b"foo"; //~ ERROR mismatched types
}


