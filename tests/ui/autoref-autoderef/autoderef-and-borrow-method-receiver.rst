tests/ui/autoref-autoderef/autoderef-and-borrow-method-receiver.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

struct Foo {
    x: isize,
}

impl Foo {
    pub fn f(&self) {}
}

fn g(x: &mut Foo) {
    x.f();
}

pub fn main() {
}


