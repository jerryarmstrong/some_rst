tests/ui/unsized-locals/by-value-trait-object-safety-rpass.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(incomplete_features)]
#![feature(unsized_locals)]

pub trait Foo {
    fn foo(self) -> String;
}

struct A;

impl Foo for A {
    fn foo(self) -> String {
        format!("hello")
    }
}

fn main() {
    let x = *(Box::new(A) as Box<dyn Foo>);
    assert_eq!(x.foo(), format!("hello"));

    // I'm not sure whether we want this to work
    let x = Box::new(A) as Box<dyn Foo>;
    assert_eq!(x.foo(), format!("hello"));
}


