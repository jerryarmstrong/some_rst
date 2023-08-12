tests/ui/span/type-annotations-needed-expr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = (vec![1,2,3]).into_iter().sum() as f64; //~ ERROR E0282
}


