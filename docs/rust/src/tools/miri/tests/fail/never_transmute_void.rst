src/tools/miri/tests/fail/never_transmute_void.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation
//@compile-flags: -Zmiri-disable-validation
//@require-annotations-for-level: ERROR

#![feature(never_type)]
#![allow(unused, invalid_value)]

mod m {
    enum VoidI {}
    pub struct Void(VoidI);

    pub fn f(v: Void) -> ! {
        match v.0 {} //~ ERROR: entering unreachable code
    }
}

fn main() {
    let v = unsafe { std::mem::transmute::<(), m::Void>(()) };
    m::f(v); //~ NOTE: inside `main`
}


