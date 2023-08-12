tests/ui/recursion/recursive-enum.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum List<T> { Cons(T, List<T>), Nil }
//~^ ERROR recursive type `List` has infinite size

fn main() {}


