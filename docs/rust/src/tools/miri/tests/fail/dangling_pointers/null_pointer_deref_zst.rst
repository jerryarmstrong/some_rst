src/tools/miri/tests/fail/dangling_pointers/null_pointer_deref_zst.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Some optimizations remove ZST accesses, thus masking this UB.
//@compile-flags: -Zmir-opt-level=0

#[allow(deref_nullptr)]
fn main() {
    let x: () = unsafe { *std::ptr::null() }; //~ ERROR: dereferencing pointer failed: null pointer is a dangling pointer
    panic!("this should never print: {:?}", x);
}


