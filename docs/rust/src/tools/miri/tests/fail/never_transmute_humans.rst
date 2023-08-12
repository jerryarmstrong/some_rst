src/tools/miri/tests/fail/never_transmute_humans.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation
//@compile-flags: -Zmiri-disable-validation

#![feature(never_type)]

struct Human;

fn main() {
    let _x: ! = unsafe {
        std::mem::transmute::<Human, !>(Human) //~ ERROR: transmuting to uninhabited
    };
}


