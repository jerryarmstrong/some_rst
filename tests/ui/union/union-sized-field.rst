tests/ui/union/union-sized-field.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::ManuallyDrop;

union Foo<T: ?Sized> {
    value: ManuallyDrop<T>,
    //~^ ERROR the size for values of type
}

struct Foo2<T: ?Sized> {
    value: ManuallyDrop<T>,
    //~^ ERROR the size for values of type
    t: u32,
}

enum Foo3<T: ?Sized> {
    Value(ManuallyDrop<T>),
    //~^ ERROR the size for values of type
}

fn main() {}


