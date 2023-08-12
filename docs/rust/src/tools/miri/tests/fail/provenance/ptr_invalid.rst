src/tools/miri/tests/fail/provenance/ptr_invalid.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(strict_provenance)]

// Ensure that a `ptr::invalid` ptr is truly invalid.
fn main() {
    let x = 42;
    let xptr = &x as *const i32;
    let xptr_invalid = std::ptr::invalid::<i32>(xptr.expose_addr());
    let _val = unsafe { *xptr_invalid }; //~ ERROR: is a dangling pointer
}


