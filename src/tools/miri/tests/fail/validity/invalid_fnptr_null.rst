src/tools/miri/tests/fail/validity/invalid_fnptr_null.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(invalid_value)]

fn main() {
    let _b: fn() = unsafe { std::mem::transmute(0usize) }; //~ ERROR: encountered a null function pointer
}


