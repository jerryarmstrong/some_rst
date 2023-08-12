src/tools/miri/tests/fail/function_calls/check_arg_abi.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    extern "Rust" {
        fn malloc(size: usize) -> *mut std::ffi::c_void;
    }

    unsafe {
        let _ = malloc(0); //~ ERROR: calling a function with ABI C using caller ABI Rust
    };
}


