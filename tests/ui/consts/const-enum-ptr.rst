tests/ui/consts/const-enum-ptr.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum E { V0, V1(isize) }
static C: &'static E = &E::V0;

pub fn main() {
    match *C {
        E::V0 => (),
        _ => panic!()
    }
}


