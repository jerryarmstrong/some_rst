tests/codegen/force-no-unwind-tables.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes -C panic=abort -C force-unwind-tables=n
// ignore-windows

#![crate_type="lib"]

// CHECK-LABEL: define{{.*}}void @foo
// CHECK-NOT: attributes #{{.*}} uwtable
#[no_mangle]
fn foo() {
    panic!();
}


