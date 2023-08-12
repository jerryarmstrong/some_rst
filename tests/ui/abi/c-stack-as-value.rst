tests/ui/abi/c-stack-as-value.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
// ignore-wasm32-bare no libc to test ffi with

#![feature(rustc_private)]

mod rustrt {
    extern crate libc;

    #[link(name = "rust_test_helpers", kind = "static")]
    extern "C" {
        pub fn rust_get_test_int() -> libc::intptr_t;
    }
}

pub fn main() {
    let _foo = rustrt::rust_get_test_int;
}


