tests/ui/associated-types/associated-types-from-supertrait.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo: Iterator<Item = i32> {}
trait Bar: Foo {}

fn main() {
    let _: &dyn Bar;
}


