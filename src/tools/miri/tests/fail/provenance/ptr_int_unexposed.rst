src/tools/miri/tests/fail/provenance/ptr_int_unexposed.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-permissive-provenance
#![feature(strict_provenance)]

fn main() {
    let x: i32 = 3;
    let x_ptr = &x as *const i32;

    let x_usize: usize = x_ptr.addr();
    // Cast back an address that did *not* get exposed.
    let ptr = std::ptr::from_exposed_addr::<i32>(x_usize);
    assert_eq!(unsafe { *ptr }, 3); //~ ERROR: is a dangling pointer
}


