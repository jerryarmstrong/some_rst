tests/ui/traits/impl-can-not-have-untraitful-items.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A { }

impl A for isize {
    const BAR: () = (); //~ ERROR const `BAR` is not a member of trait `A`
    type Baz = (); //~ ERROR type `Baz` is not a member of trait `A`
    fn foo(&self) { } //~ ERROR method `foo` is not a member of trait `A`
}

fn main() { }


