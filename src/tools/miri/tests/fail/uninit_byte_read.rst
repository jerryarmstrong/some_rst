src/tools/miri/tests/fail/uninit_byte_read.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-stacked-borrows
fn main() {
    let v: Vec<u8> = Vec::with_capacity(10);
    let undef = unsafe { *v.get_unchecked(5) }; //~ ERROR: uninitialized
    let x = undef + 1;
    panic!("this should never print: {}", x);
}


