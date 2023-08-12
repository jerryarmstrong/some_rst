src/tools/miri/tests/fail/validity/uninit_raw_ptr.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]

fn main() {
    // The array avoids a `Scalar` layout which detects uninit without even doing validation.
    let _val = unsafe { std::mem::MaybeUninit::<[*const u8; 1]>::uninit().assume_init() };
    //~^ ERROR: uninitialized
}


