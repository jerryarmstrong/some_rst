tests/ui/unsized-locals/by-value-trait-object-safety.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_locals)]
//~^ WARN the feature `unsized_locals` is incomplete

pub trait Foo {
    fn foo(self) -> String
    where
        Self: Sized;
}

struct A;

impl Foo for A {
    fn foo(self) -> String {
        format!("hello")
    }
}

fn main() {
    let x = *(Box::new(A) as Box<dyn Foo>);
    x.foo();
    //~^ERROR the `foo` method cannot be invoked on a trait object
}


