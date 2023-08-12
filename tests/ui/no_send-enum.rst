tests/ui/no_send-enum.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Send;

struct NoSend;
impl !Send for NoSend {}

enum Foo {
    A(NoSend)
}

fn bar<T: Send>(_: T) {}

fn main() {
    let x = Foo::A(NoSend);
    bar(x);
    //~^ ERROR `NoSend` cannot be sent between threads safely
}


