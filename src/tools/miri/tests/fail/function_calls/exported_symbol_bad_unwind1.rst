src/tools/miri/tests/fail/function_calls/exported_symbol_bad_unwind1.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-abi-check
#![feature(c_unwind)]

#[no_mangle]
extern "C-unwind" fn unwind() {
    panic!();
}

fn main() {
    extern "C" {
        fn unwind();
    }
    unsafe { unwind() }
    //~^ ERROR: unwinding past a stack frame that does not allow unwinding
}


