tests/ui/abi/cross-crate/auxiliary/anon-extern-mod-cross-crate-1.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "anonexternmod"]
#![feature(rustc_private)]

extern crate libc;

#[link(name = "rust_test_helpers", kind = "static")]
extern "C" {
    pub fn rust_get_test_int() -> libc::intptr_t;
}


