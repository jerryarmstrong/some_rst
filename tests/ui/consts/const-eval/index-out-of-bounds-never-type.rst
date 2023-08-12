tests/ui/consts/const-eval/index-out-of-bounds-never-type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

// Regression test for #66975
#![warn(unconditional_panic)]
#![feature(never_type)]

struct PrintName<T>(T);

impl<T> PrintName<T> {
    const VOID: ! = { let x = 0 * std::mem::size_of::<T>(); [][x] };
    //~^ ERROR evaluation of `PrintName::<()>::VOID` failed

}

fn f<T>() {
    let _ = PrintName::<T>::VOID;
}

pub fn main() {
    f::<()>();
}


