tests/ui/abi/anon-extern-mod.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
// ignore-wasm32-bare no libc to test ffi with

#![feature(rustc_private)]

extern crate libc;

#[link(name = "rust_test_helpers", kind = "static")]
extern "C" {
    fn rust_get_test_int() -> libc::intptr_t;
}

pub fn main() {
    unsafe {
        let _ = rust_get_test_int();
    }
}


