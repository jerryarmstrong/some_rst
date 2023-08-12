tests/ui/missing-trait-bounds/missing-trait-bounds-for-method-call.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Default, PartialEq)]
struct Foo<T> {
    bar: Box<[T]>,
}

trait Bar {
    fn foo(&self) {}
}

impl<T: Default + Bar> Bar for Foo<T> {}

impl<T> Foo<T> {
    fn bar(&self) {
        self.foo();
        //~^ ERROR the method
    }
}

struct Fin<T> where T: Bar {
    bar: Box<[T]>,
}

impl<T: Default + Bar> Bar for Fin<T> {}

impl<T: Bar> Fin<T> {
    fn bar(&self) {
        self.foo();
        //~^ ERROR the method
    }
}
fn main() {}


