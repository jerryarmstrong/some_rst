tests/ui/impl-trait/in-trait/nested-rpitit.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

use std::fmt::Display;
use std::ops::Deref;

trait Foo {
    fn bar(self) -> impl Deref<Target = impl Display + ?Sized>;
}

struct A;

impl Foo for A {
    fn bar(self) -> &'static str {
        "Hello, world"
    }
}

struct B;

impl Foo for B {
    fn bar(self) -> Box<i32> {
        Box::new(42)
    }
}

fn main() {
    println!("Message for you: {:?}", &*A.bar());
    println!("Another for you: {:?}", &*B.bar());
}


