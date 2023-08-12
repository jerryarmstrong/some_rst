src/tools/miri/tests/fail/function_calls/check_arg_count_too_few_args.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    extern "C" {
        fn malloc() -> *mut std::ffi::c_void;
    }

    unsafe {
        let _ = malloc(); //~ ERROR: Undefined Behavior: incorrect number of arguments: got 0, expected 1
    };
}


