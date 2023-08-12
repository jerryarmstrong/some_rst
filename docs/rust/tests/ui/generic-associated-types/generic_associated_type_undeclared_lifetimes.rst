tests/ui/generic-associated-types/generic_associated_type_undeclared_lifetimes.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Deref;

trait Iterable {
    type Item<'a>;
    type Iter<'a>: Iterator<Item = Self::Item<'a>>
        + Deref<Target = Self::Item<'b>>;
    //~^ ERROR undeclared lifetime

    fn iter<'a>(&'a self) -> Self::Iter<'undeclared>;
    //~^ ERROR undeclared lifetime
}

fn main() {}


