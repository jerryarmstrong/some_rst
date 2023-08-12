tests/ui/associated-type-bounds/handle-predicates-that-can-define-assoc-type.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Foo<T> {}
trait Bar {
    type A;
    type B;
}
trait Baz: Bar<B = u32> + Foo<Self::A> {}

fn main() {}


