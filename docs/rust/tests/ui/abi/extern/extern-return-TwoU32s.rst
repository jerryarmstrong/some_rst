tests/ui/abi/extern/extern-return-TwoU32s.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(improper_ctypes)]

// ignore-wasm32-bare no libc to test ffi with

pub struct TwoU32s {
    one: u32,
    two: u32,
}

#[link(name = "rust_test_helpers", kind = "static")]
extern "C" {
    pub fn rust_dbg_extern_return_TwoU32s() -> TwoU32s;
}

pub fn main() {
    unsafe {
        let y = rust_dbg_extern_return_TwoU32s();
        assert_eq!(y.one, 10);
        assert_eq!(y.two, 20);
    }
}


