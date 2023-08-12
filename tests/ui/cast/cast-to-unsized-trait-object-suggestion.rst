tests/ui/cast/cast-to-unsized-trait-object-suggestion.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    &1 as dyn Send; //~ ERROR cast to unsized
    Box::new(1) as dyn Send; //~ ERROR cast to unsized
}


