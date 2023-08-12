tests/ui/hygiene/expansion-info-reset.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format_args!({ #[derive(Clone)] struct S; });
    //~^ ERROR format argument must be a string literal
}


