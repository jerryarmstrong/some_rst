tests/codegen/issue-98294-get-mut-copy-from-slice-opt.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // min-llvm-version: 15.0.0
// ignore-debug: The debug assertions get in the way
// compile-flags: -O

#![crate_type = "lib"]

// There should be no calls to panic / len_mismatch_fail.

#[no_mangle]
pub fn test(a: &mut [u8], offset: usize, bytes: &[u8]) {
    // CHECK-LABEL: @test(
    // CHECK-NOT: call
    // CHECK: call void @llvm.memcpy
    // CHECK-NOT: call
    // CHECK: }
    if let Some(dst) = a.get_mut(offset..offset + bytes.len()) {
        dst.copy_from_slice(bytes);
    }
}


