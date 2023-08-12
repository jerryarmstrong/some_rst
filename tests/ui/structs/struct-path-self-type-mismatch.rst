tests/ui/structs/struct-path-self-type-mismatch.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<A> { inner: A }

trait Bar { fn bar(); }

impl Bar for Foo<i32> {
    fn bar() {
        Self { inner: 1.5f32 }; //~ ERROR mismatched types
    }
}

impl<T> Foo<T> {
    fn new<U>(u: U) -> Foo<U> {
        Self {
        //~^ ERROR mismatched types
            inner: u
            //~^ ERROR mismatched types
        }
    }
}

fn main() {}


