tests/codegen/unwind-abis/nounwind.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C opt-level=0 -Cpanic=abort
// ignore-wasm32-bare compiled with panic=abort by default

#![crate_type = "lib"]
#![feature(c_unwind)]

// We disable optimizations to prevent LLVM from inferring the attribute.

// CHECK: Function Attrs:{{.*}}nounwind
// CHECK-NEXT: @foo
#[no_mangle]
pub extern "C" fn foo() {}

// CHECK: Function Attrs:{{.*}}nounwind
// CHECK-NEXT: @bar
#[no_mangle]
pub fn bar() {}


