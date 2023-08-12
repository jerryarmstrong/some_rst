src/tools/miri/tests/fail/invalid_int.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]
// Validation makes this fail in the wrong place
// Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

fn main() {
    let i = unsafe { std::mem::MaybeUninit::<i32>::uninit().assume_init() }; //~ ERROR: uninitialized
    let _x = i + 0;
}


