tests/ui/parser/issues/issue-102182-impl-trait-recover.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: impl Trait>() {}
//~^ ERROR expected trait bound, found `impl Trait` type
fn main() {}


