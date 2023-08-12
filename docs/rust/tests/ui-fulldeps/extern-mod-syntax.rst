tests/ui-fulldeps/extern-mod-syntax.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
#![feature(rustc_private)]

extern crate libc;
use libc::c_void;

pub fn main() {
    println!("Hello world!");
}


