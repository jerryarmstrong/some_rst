tests/ui/traits/default-method/auxiliary/xc_2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:xc.rs

extern crate xc as aux;
use aux::A;

pub struct a_struct { pub x: isize }

impl A for a_struct {
    fn f(&self) -> isize { 10 }
}

// This function will need to get inlined, and badness may result.
pub fn welp<A>(x: A) -> A {
    let a = a_struct { x: 0 };
    a.g();
    x
}


