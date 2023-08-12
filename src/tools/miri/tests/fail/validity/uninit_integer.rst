src/tools/miri/tests/fail/validity/uninit_integer.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]
// This test is from https://github.com/rust-lang/miri/issues/1340#issue-600900312.

fn main() {
    // The array avoids a `Scalar` layout which detects uninit without even doing validation.
    let _val = unsafe { std::mem::MaybeUninit::<[usize; 1]>::uninit().assume_init() };
    //~^ ERROR: uninitialized
}


