tests/ui/consts/const-enum-byref.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum E { V, VV(isize) }
static C: E = E::V;

fn f(a: &E) {
    match *a {
        E::V => {}
        E::VV(..) => panic!()
    }
}

pub fn main() {
    f(&C)
}


