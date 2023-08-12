src/tools/miri/tests/fail/panic/bad_unwind.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(c_unwind)]

//! Unwinding when the caller ABI is "C" (without "-unwind") is UB.

extern "C-unwind" fn unwind() {
    panic!();
}

fn main() {
    let unwind: extern "C-unwind" fn() = unwind;
    let unwind: extern "C" fn() = unsafe { std::mem::transmute(unwind) };
    std::panic::catch_unwind(|| unwind()).unwrap_err();
    //~^ ERROR: unwinding past a stack frame that does not allow unwinding
}


