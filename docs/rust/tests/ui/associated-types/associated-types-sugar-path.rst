tests/ui/associated-types/associated-types-sugar-path.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_imports)]
// Test paths to associated types using the type-parameter-only sugar.

use std::ops::Deref;

pub trait Foo {
    type A;
    fn boo(&self) -> Self::A;
}

impl Foo for isize {
    type A = usize;
    fn boo(&self) -> usize {
        5
    }
}

// Using a type via a function.
pub fn bar<T: Foo>(a: T, x: T::A) -> T::A {
    let _: T::A = a.boo();
    x
}

// Using a type via an impl.
trait C {
    fn f();
    fn g(&self) { }
}
struct B<X>(X);
impl<T: Foo> C for B<T> {
    fn f() {
        let x: T::A = panic!();
    }
}

pub fn main() {
    let z: usize = bar(2, 4);
}


