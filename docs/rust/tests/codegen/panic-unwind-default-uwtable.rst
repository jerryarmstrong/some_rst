tests/codegen/panic-unwind-default-uwtable.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C panic=unwind -C no-prepopulate-passes

#![crate_type = "lib"]

// CHECK: attributes #{{.*}} uwtable
pub fn foo() {}


