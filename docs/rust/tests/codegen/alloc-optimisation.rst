tests/codegen/alloc-optimisation.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// no-system-llvm
// compile-flags: -O
#![crate_type="lib"]

#[no_mangle]
pub fn alloc_test(data: u32) {
    // CHECK-LABEL: @alloc_test
    // CHECK-NEXT: start:
    // CHECK-NEXT: ret void
    let x = Box::new(data);
    drop(x);
}


