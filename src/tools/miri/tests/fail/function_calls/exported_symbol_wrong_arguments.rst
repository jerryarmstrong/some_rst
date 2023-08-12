src/tools/miri/tests/fail/function_calls/exported_symbol_wrong_arguments.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
fn foo() {}

fn main() {
    extern "Rust" {
        fn foo(_: i32);
    }
    unsafe { foo(1) } //~ ERROR: calling a function with more arguments than it expected
}


