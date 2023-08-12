tests/ui/parser/doc-inside-trait-item.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait User{
    fn test();
    /// empty doc
    //~^ ERROR found a documentation comment that doesn't document anything
}
fn main() {}


