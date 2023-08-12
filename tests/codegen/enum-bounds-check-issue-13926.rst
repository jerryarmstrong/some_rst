tests/codegen/enum-bounds-check-issue-13926.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks an optimization that is not guaranteed to work. This test case should not block
// a future LLVM update.
// compile-flags: -O

#![crate_type = "lib"]

#[repr(u8)]
pub enum Exception {
    Low = 5,
    High = 10,
}

// CHECK-LABEL: @access
#[no_mangle]
pub fn access(array: &[usize; 12], exc: Exception) -> usize {
    // CHECK-NOT: panic_bounds_check
    array[(exc as u8 - 4) as usize]
}


