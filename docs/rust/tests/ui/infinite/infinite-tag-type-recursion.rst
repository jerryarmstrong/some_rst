tests/ui/infinite/infinite-tag-type-recursion.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum MList { Cons(isize, MList), Nil }
//~^ ERROR recursive type `MList` has infinite size

fn main() { let a = MList::Cons(10, MList::Cons(11, MList::Nil)); }


