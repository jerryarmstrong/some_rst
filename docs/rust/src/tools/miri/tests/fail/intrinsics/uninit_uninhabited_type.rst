src/tools/miri/tests/fail/intrinsics/uninit_uninhabited_type.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]

#[allow(deprecated, invalid_value)]
fn main() {
    unsafe { std::mem::uninitialized::<!>() };
    //~^ ERROR: attempted to instantiate uninhabited type `!`
}


