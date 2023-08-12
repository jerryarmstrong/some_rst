tests/ui/layout/thin-meta-implies-thin-ptr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(ptr_metadata)]

use std::ptr::Thin;

fn main() {}

fn foo<T: ?Sized + Thin>(t: *const T) -> *const () {
    unsafe { std::mem::transmute(t) }
}


