tests/ui/traits/no_send-struct.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Send;

struct Foo {
    a: isize,
}

impl !Send for Foo {}

fn bar<T: Send>(_: T) {}

fn main() {
    let x = Foo { a: 5 };
    bar(x);
    //~^ ERROR `Foo` cannot be sent between threads safely
}


