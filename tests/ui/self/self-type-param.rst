tests/ui/self/self-type-param.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(dead_code)]
// pretty-expanded FIXME #23616

trait MyTrait {
    fn f(&self) -> Self;
}

struct S {
    x: isize
}

impl MyTrait for S {
    fn f(&self) -> S {
        S { x: 3 }
    }
}

pub fn main() {}


