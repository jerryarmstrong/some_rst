tests/ui/traits/bad-method-typaram-kind.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T:'static>() {
    1.bar::<T>(); //~ ERROR `T` cannot be sent between threads safely
}

trait Bar {
    fn bar<T:Send>(&self);
}

impl Bar for usize {
    fn bar<T:Send>(&self) {
    }
}

fn main() {}


