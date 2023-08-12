tests/ui/issues/issue-7246.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_code)]
#![allow(dead_code)]

use std::ptr;
pub unsafe fn g() {
    return;
    if *ptr::null() {}; //~ ERROR unreachable
    //~| WARNING dereferencing a null pointer
}

pub fn main() {}


