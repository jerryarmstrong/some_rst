tests/ui/traits/inheritance/cross-trait-call-xc.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:xc_call.rs


extern crate xc_call as aux;

use aux::Foo;

trait Bar : Foo {
    fn g(&self) -> isize;
}

impl Bar for aux::A {
    fn g(&self) -> isize { self.f() }
}

pub fn main() {
    let a = &aux::A { x: 3 };
    assert_eq!(a.g(), 10);
}


