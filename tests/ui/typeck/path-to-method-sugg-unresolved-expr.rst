tests/ui/typeck/path-to-method-sugg-unresolved-expr.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let page_size = page_size::get();
    //~^ ERROR failed to resolve: use of undeclared crate or module `page_size`
}


