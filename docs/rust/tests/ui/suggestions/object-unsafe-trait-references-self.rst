tests/ui/suggestions/object-unsafe-trait-references-self.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {
    fn baz(&self, _: Self) {}
    fn bat(&self) -> Self {}
}

fn bar(x: &dyn Trait) {} //~ ERROR the trait `Trait` cannot be made into an object

trait Other: Sized {}

fn foo(x: &dyn Other) {} //~ ERROR the trait `Other` cannot be made into an object

fn main() {}


