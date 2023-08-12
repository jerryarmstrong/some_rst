tests/codegen/nounwind.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:nounwind.rs
// compile-flags: -C no-prepopulate-passes -C panic=abort -C metadata=a
// ignore-windows
// ignore-android

#![crate_type = "lib"]

extern crate nounwind;

#[no_mangle]
pub fn foo() {
    nounwind::bar();
// CHECK: @foo() unnamed_addr #0
// CHECK: @bar() unnamed_addr #0
// CHECK: attributes #0 = { {{.*}}nounwind{{.*}} }
}


