src/tools/miri/tests/fail/dangling_pointers/null_pointer_write_zst.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Some optimizations remove ZST accesses, thus masking this UB.
//@compile-flags: -Zmir-opt-level=0

#[allow(deref_nullptr)]
fn main() {
    // Not using the () type here, as writes of that type do not even have MIR generated.
    // Also not assigning directly as that's array initialization, not assignment.
    let zst_val = [1u8; 0];
    unsafe { std::ptr::null_mut::<[u8; 0]>().write(zst_val) };
    //~^ERROR: memory access failed: null pointer is a dangling pointer
}


