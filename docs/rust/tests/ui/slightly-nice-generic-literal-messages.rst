tests/ui/slightly-nice-generic-literal-messages.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker;

struct Foo<T,U>(T, marker::PhantomData<U>);

fn main() {
    match Foo(1.1, marker::PhantomData) {
        1 => {}
    //~^ ERROR mismatched types
    //~| expected struct `Foo<{float}, _>`
    //~| found type `{integer}`
    //~| expected struct `Foo`, found integer
    }

}


