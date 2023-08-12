tests/ui/auxiliary/using-target-feature-unstable.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(avx512_target_feature)]

#[inline]
#[target_feature(enable = "avx512ifma")]
pub unsafe fn foo() {}


