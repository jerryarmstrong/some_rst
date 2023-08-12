tests/ui/hygiene/hygiene-dodging-1.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]

mod x {
    pub fn g() -> usize {14}
}

pub fn main(){
    // should *not* shadow the module x:
    let x = 9;
    // use it to avoid warnings:
    x+3;
    assert_eq!(x::g(),14);
}


