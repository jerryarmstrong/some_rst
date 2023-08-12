tests/ui/non-copyable-void.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-wasm32-bare no libc to test ffi with

#![feature(rustc_private)]

extern crate libc;

fn main() {
    let x : *const Vec<isize> = &vec![1,2,3];
    let y : *const libc::c_void = x as *const libc::c_void;
    unsafe {
        let _z = (*y).clone();
        //~^ ERROR no method named `clone` found
    }
}


