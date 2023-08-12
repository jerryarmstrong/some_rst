tests/codegen/cfguard-non-msvc.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C control-flow-guard
// ignore-msvc

#![crate_type = "lib"]

// A basic test function.
pub fn test() {
}

// Ensure the cfguard module flag is not added for non-MSVC targets.
// CHECK-NOT: !"cfguard"


