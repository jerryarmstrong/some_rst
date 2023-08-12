tests/ui/pattern/pattern-ident-path-generics.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match Some("foo") {
        None::<isize> => {}   //~ ERROR mismatched types
        Some(_) => {}
    }
}


