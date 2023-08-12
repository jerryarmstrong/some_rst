tests/ui/issues/issue-1251.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(unused_attributes)]
#![allow(dead_code)]
// pretty-expanded FIXME #23616
// ignore-wasm32-bare no libc to test ffi with
#![feature(rustc_private)]

mod rustrt {
    extern crate libc;

    extern "C" {
        pub fn rust_get_test_int() -> libc::intptr_t;
    }
}

pub fn main() {}


