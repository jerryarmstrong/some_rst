tests/ui/abi/extern/extern-return-TwoU16s.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(improper_ctypes)]

// ignore-wasm32-bare no libc to test ffi with

pub struct TwoU16s {
    one: u16,
    two: u16,
}

#[link(name = "rust_test_helpers", kind = "static")]
extern "C" {
    pub fn rust_dbg_extern_return_TwoU16s() -> TwoU16s;
}

pub fn main() {
    unsafe {
        let y = rust_dbg_extern_return_TwoU16s();
        assert_eq!(y.one, 10);
        assert_eq!(y.two, 20);
    }
}


