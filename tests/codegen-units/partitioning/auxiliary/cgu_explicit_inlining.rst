tests/codegen-units/partitioning/auxiliary/cgu_explicit_inlining.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[inline]
pub fn inlined() {}

#[inline(always)]
pub fn always_inlined() {}

#[inline(never)]
pub fn never_inlined() {}


