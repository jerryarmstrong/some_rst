tests/ui/maybe-bounds.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Tr: ?Sized {}
//~^ ERROR `?Trait` is not permitted in supertraits

type A1 = dyn Tr + (?Sized);
//~^ ERROR `?Trait` is not permitted in trait object types
type A2 = dyn for<'a> Tr + (?Sized);
//~^ ERROR `?Trait` is not permitted in trait object types

fn main() {}


