tests/ui/lexical-scopes.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct T { i: i32 }
fn f<T>() {
    let t = T { i: 0 }; //~ ERROR expected struct, variant or union type, found type parameter `T`
}

mod Foo {
    pub fn f() {}
}
fn g<Foo>() {
    Foo::f(); //~ ERROR no function or associated item named `f`
}

fn main() {}


