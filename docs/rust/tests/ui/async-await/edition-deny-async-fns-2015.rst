tests/ui/async-await/edition-deny-async-fns-2015.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015

async fn foo() {} //~ ERROR `async fn` is not permitted in Rust 2015

fn baz() { async fn foo() {} } //~ ERROR `async fn` is not permitted in Rust 2015

async fn async_baz() { //~ ERROR `async fn` is not permitted in Rust 2015
    async fn bar() {} //~ ERROR `async fn` is not permitted in Rust 2015
}

struct Foo {}

impl Foo {
    async fn foo() {} //~ ERROR `async fn` is not permitted in Rust 2015
}

trait Bar {
    async fn foo() {} //~ ERROR `async fn` is not permitted in Rust 2015
    //~^ ERROR functions in traits cannot be declared `async`
}

fn main() {
    macro_rules! accept_item { ($x:item) => {} }

    accept_item! {
        async fn foo() {} //~ ERROR `async fn` is not permitted in Rust 2015
    }

    accept_item! {
        impl Foo {
            async fn bar() {} //~ ERROR `async fn` is not permitted in Rust 2015
        }
    }

    let inside_closure = || {
        async fn bar() {} //~ ERROR `async fn` is not permitted in Rust 2015
    };
}


