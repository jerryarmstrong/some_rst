src/tools/miri/tests/fail/function_calls/exported_symbol_wrong_type.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
static FOO: () = ();

fn main() {
    extern "C" {
        fn FOO();
    }
    unsafe { FOO() } //~ ERROR: attempt to call an exported symbol that is not defined as a function
}


