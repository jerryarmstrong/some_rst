src/tools/miri/tests/fail/function_calls/check_arg_count_too_many_args.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    extern "C" {
        fn malloc(_: i32, _: i32) -> *mut std::ffi::c_void;
    }

    unsafe {
        let _ = malloc(1, 2); //~ ERROR: Undefined Behavior: incorrect number of arguments: got 2, expected 1
    };
}


