tests/ui/self/arbitrary_self_types_pin_lifetime_impl_trait-async.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use std::pin::Pin;

struct Foo;

impl Foo {
    async fn f(self: Pin<&Self>) -> impl Clone { self }
    //~^ ERROR: captures lifetime that does not appear in bounds
}

fn main() {
    { Pin::new(&Foo).f() };
}


