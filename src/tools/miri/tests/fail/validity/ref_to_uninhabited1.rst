src/tools/miri/tests/fail/validity/ref_to_uninhabited1.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
use std::mem::{forget, transmute};

fn main() {
    unsafe {
        let x: Box<!> = transmute(&mut 42); //~ERROR: encountered a box pointing to uninhabited type !
        forget(x);
    }
}


