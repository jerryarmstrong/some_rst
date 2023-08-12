src/tools/miri/tests/fail/dangling_pointers/wild_pointer_deref.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-permissive-provenance

fn main() {
    let p = 44 as *const i32;
    let x = unsafe { *p }; //~ ERROR: is a dangling pointer
    panic!("this should never print: {}", x);
}


