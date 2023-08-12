tests/ui/repr/issue-83505-repr-simd.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for the ICE described in #83505.

#![crate_type="lib"]

#[repr(simd)]
//~^ ERROR: attribute should be applied to a struct [E0517]
//~| ERROR: unsupported representation for zero-variant enum [E0084]
enum Es {}
static CLs: Es;
//~^ ERROR: free static item without body


