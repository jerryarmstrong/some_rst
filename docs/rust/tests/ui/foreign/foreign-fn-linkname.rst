tests/ui/foreign/foreign-fn-linkname.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-wasm32-bare no libc to test ffi with
// ignore-sgx no libc

#![feature(rustc_private)]

extern crate libc;
use std::ffi::CString;

mod mlibc {
    use libc::{c_char, size_t};

    extern "C" {
        #[link_name = "strlen"]
        pub fn my_strlen(str: *const c_char) -> size_t;
    }
}

fn strlen(str: String) -> usize {
    // C string is terminated with a zero
    let s = CString::new(str).unwrap();
    unsafe { mlibc::my_strlen(s.as_ptr()) as usize }
}

pub fn main() {
    let len = strlen("Rust".to_string());
    assert_eq!(len, 4);
}


