tests/ui/sized/recursive-type-2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
//~^ ERROR cycle detected when computing layout of `Foo<()>`

trait A { type Assoc: ?Sized; }

impl A for () {
    type Assoc = Foo<()>;
}
struct Foo<T: A>(T::Assoc);

fn main() {
    let x: Foo<()>;
}


