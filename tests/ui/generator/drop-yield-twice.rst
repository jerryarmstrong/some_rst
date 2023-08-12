tests/ui/generator/drop-yield-twice.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls, generators)]

struct Foo(i32);
impl !Send for Foo {}

fn main() {
    assert_send(|| { //~ ERROR generator cannot be sent between threads safely
        let guard = Foo(42);
        yield;
        drop(guard);
        yield;
    })
}

fn assert_send<T: Send>(_: T) {}


