tests/codegen/vec-optimizes-away.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-debug: the debug assertions get in the way
// no-system-llvm
// compile-flags: -O
#![crate_type="lib"]

#[no_mangle]
pub fn sum_me() -> i32 {
    // CHECK-LABEL: @sum_me
    // CHECK-NEXT: {{^.*:$}}
    // CHECK-NEXT: ret i32 6
    vec![1, 2, 3].iter().sum::<i32>()
}


