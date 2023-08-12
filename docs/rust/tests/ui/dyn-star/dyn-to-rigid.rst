tests/ui/dyn-star/dyn-to-rigid.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(dyn_star)]
#![allow(incomplete_features)]

trait Tr {}

fn f(x: dyn* Tr) -> usize {
    x as usize
    //~^ ERROR casting `(dyn* Tr + 'static)` as `usize` is invalid
}

fn main() {}


