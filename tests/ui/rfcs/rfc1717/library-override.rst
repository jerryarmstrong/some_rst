tests/ui/rfcs/rfc1717/library-override.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-wasm32-bare no libc to test ffi with
// compile-flags: -lstatic=wronglibrary:rust_test_helpers

#[link(name = "wronglibrary", kind = "dylib")]
extern "C" {
    pub fn rust_dbg_extern_identity_u32(x: u32) -> u32;
}

fn main() {
    unsafe {
        rust_dbg_extern_identity_u32(42);
    }
}


