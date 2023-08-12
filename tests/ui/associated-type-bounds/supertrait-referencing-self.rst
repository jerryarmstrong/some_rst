tests/ui/associated-type-bounds/supertrait-referencing-self.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
trait Foo {
    type Bar;
}
trait Qux: Foo + AsRef<Self::Bar> {}
trait Foo2 {}

trait Qux2: Foo2 + AsRef<Self::Bar> {
    type Bar;
}

fn main() {}


