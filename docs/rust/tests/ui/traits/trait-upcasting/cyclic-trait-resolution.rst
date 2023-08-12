tests/ui/traits/trait-upcasting/cyclic-trait-resolution.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A: B + A {}
//~^ ERROR cycle detected when computing the super predicates of `A` [E0391]

trait B {}

impl A for () {}

impl B for () {}

fn main() {
    let a: Box<dyn A> = Box::new(());
    let _b: Box<dyn B> = a;
}


