tests/ui/dyn-star/return.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(dyn_star)]
//~^ WARN the feature `dyn_star` is incomplete and may not be safe to use and/or cause compiler crashes

fn _foo() -> dyn* Unpin {
    4usize
}

fn main() {}


