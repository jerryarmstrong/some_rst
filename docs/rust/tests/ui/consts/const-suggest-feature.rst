tests/ui/consts/const-suggest-feature.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const WRITE: () = unsafe {
    *std::ptr::null_mut() = 0;
    //~^ ERROR dereferencing raw mutable pointers in constants is unstable
    //~| HELP add `#![feature(const_mut_refs)]` to the crate attributes to enable
};

fn main() {}


