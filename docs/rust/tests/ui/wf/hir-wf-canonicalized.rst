tests/ui/wf/hir-wf-canonicalized.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // incremental

trait Foo {
    type V;
}

trait Callback<T: Foo>: Fn(&Bar<'_, T>, &T::V) {}

struct Bar<'a, T> {
    callback: Box<dyn Callback<dyn Callback<Bar<'a, T>>>>,
    //~^ ERROR the trait bound `Bar<'a, T>: Foo` is not satisfied
    //~| ERROR the trait bound `(dyn Callback<Bar<'a, T>, for<'b, 'c, 'd> Output = ()> + 'static): Foo` is not satisfied
    //~| ERROR the size for values of type `(dyn Callback<Bar<'a, T>, for<'b, 'c, 'd> Output = ()> + 'static)` cannot be known at compilation time
}

impl<T: Foo> Bar<'_, Bar<'_, T>> {}

fn main() {}


