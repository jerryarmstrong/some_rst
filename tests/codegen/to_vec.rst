tests/codegen/to_vec.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![crate_type = "lib"]

// CHECK-LABEL: @copy_to_vec
#[no_mangle]
fn copy_to_vec(s: &[u64]) -> Vec<u64> {
  s.to_vec()
  // CHECK: call void @llvm.memcpy
}


