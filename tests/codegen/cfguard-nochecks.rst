tests/codegen/cfguard-nochecks.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C control-flow-guard=nochecks
// only-msvc

#![crate_type = "lib"]

// A basic test function.
pub fn test() {
}

// Ensure the module flag cfguard=1 is present
// CHECK: !"cfguard", i32 1


