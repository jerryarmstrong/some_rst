src/tools/miri/tests/fail/function_calls/exported_symbol_shim_clashing.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
extern "C" fn malloc(_: usize) -> *mut std::ffi::c_void {
    //~^ HELP: the `malloc` symbol is defined here
    unreachable!()
}

fn main() {
    extern "C" {
        fn malloc(_: usize) -> *mut std::ffi::c_void;
    }
    unsafe {
        malloc(0);
        //~^ ERROR: found `malloc` symbol definition that clashes with a built-in shim
    }
}


