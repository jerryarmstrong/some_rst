src/tools/miri/tests/fail/panic/bad_miri_start_panic.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-abi-check
// This feature is required to trigger the error using the "C" ABI.
#![feature(c_unwind)]

extern "C" {
    fn miri_start_panic(payload: *mut u8) -> !;
}

fn main() {
    unsafe { miri_start_panic(&mut 0) }
    //~^ ERROR: unwinding past a stack frame that does not allow unwinding
}


