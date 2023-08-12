src/tools/miri/tests/fail/static_memory_modification2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Stacked Borrows detects that we are casting & to &mut and so it changes why we fail
//@compile-flags: -Zmiri-disable-stacked-borrows

use std::mem::transmute;

#[allow(mutable_transmutes)]
fn main() {
    unsafe {
        let s = "this is a test";
        transmute::<&[u8], &mut [u8]>(s.as_bytes())[4] = 42; //~ ERROR: read-only
    }
}


