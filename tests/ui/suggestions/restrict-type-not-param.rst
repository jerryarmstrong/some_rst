tests/ui/suggestions/restrict-type-not-param.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Add;

struct Wrapper<T>(T);

trait Foo {}

fn qux<T>(a: Wrapper<T>, b: T) -> T {
    a + b
    //~^ ERROR cannot add `T` to `Wrapper<T>`
}

fn main() {}


