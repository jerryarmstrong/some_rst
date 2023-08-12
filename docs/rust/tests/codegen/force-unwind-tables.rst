tests/codegen/force-unwind-tables.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes -C force-unwind-tables=y

#![crate_type="lib"]

// CHECK: attributes #{{.*}} uwtable
pub fn foo() {}


