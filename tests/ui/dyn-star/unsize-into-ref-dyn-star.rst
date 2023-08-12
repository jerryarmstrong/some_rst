tests/ui/dyn-star/unsize-into-ref-dyn-star.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(dyn_star)]
#![allow(incomplete_features)]

use std::fmt::Debug;

fn main() {
    let i = 42 as &dyn* Debug;
    //~^ ERROR non-primitive cast: `i32` as `&dyn* Debug`
}


