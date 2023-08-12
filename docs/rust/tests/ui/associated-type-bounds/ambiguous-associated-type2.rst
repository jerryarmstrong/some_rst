tests/ui/associated-type-bounds/ambiguous-associated-type2.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Item;
}
trait Bar<T> {
    type Item;
}
trait Baz: Foo + Bar<Self::Item> {}
//~^ ERROR cycle detected when computing the super traits of `Baz` with associated type name `Item` [E0391]

fn main() {}


