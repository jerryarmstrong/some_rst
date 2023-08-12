tests/ui/consts/const-enum-structlike.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum E {
    S0 { s: String },
    S1 { u: usize }
}

static C: E = E::S1 { u: 23 };

pub fn main() {
    match C {
        E::S0 { .. } => panic!(),
        E::S1 { u } => assert_eq!(u, 23)
    }
}


