tests/ui/impl-trait/nesting.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

fn foo<T>(t: T) -> impl Into<[T; { const FOO: usize = 1; FOO }]> {
    [t]
}

fn bar() -> impl Into<[u8; { const FOO: usize = 1; FOO }]> {
    [99]
}

fn main() {
    println!("{:?}", foo(42).into());
    println!("{:?}", bar().into());
}


