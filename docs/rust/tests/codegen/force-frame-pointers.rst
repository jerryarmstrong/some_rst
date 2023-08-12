tests/codegen/force-frame-pointers.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes -C force-frame-pointers=y

#![crate_type="lib"]

// CHECK: attributes #{{.*}} "frame-pointer"="all"
pub fn foo() {}


