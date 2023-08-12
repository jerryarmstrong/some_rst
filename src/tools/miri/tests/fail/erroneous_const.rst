src/tools/miri/tests/fail/erroneous_const.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Make sure we detect erroneous constants post-monomorphization even when they are unused.
//! (https://github.com/rust-lang/miri/issues/1382)
// Inlining changes the error location
//@compile-flags: -Zmir-opt-level=0
#![feature(never_type)]

struct PrintName<T>(T);
impl<T> PrintName<T> {
    const VOID: ! = panic!(); //~ERROR: evaluation of `PrintName::<i32>::VOID` failed
}

fn no_codegen<T>() {
    if false {
        let _ = PrintName::<T>::VOID; //~NOTE: constant
    }
}
fn main() {
    no_codegen::<i32>();
}


