tests/ui/abi/cabi-int-widening.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-wasm32-bare no libc to test ffi with

#[link(name = "rust_test_helpers", kind = "static")]
extern "C" {
    fn rust_int8_to_int32(_: i8) -> i32;
}

fn main() {
    let x = unsafe {
        rust_int8_to_int32(-1)
    };

    assert!(x == -1);
}


