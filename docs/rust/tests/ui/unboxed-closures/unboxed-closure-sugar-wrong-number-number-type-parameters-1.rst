tests/ui/unboxed-closures/unboxed-closure-sugar-wrong-number-number-type-parameters-1.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures)]

trait One<A> { fn foo(&self) -> A; }

fn foo(_: &dyn One()) //~ ERROR associated type `Output` not found for `One<()>`
{}

fn main() { }


