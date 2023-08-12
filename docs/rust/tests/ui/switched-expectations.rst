tests/ui/switched-expectations.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let var = 10i32;
    let ref string: String = var; //~ ERROR mismatched types [E0308]
}


