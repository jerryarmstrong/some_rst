src/tools/miri/tests/fail/function_calls/check_arg_count_abort.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    extern "C" {
        fn abort(_: i32) -> !;
    }

    unsafe {
        abort(1);
        //~^ ERROR: Undefined Behavior: incorrect number of arguments: got 1, expected 0
    }
}


