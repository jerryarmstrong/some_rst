tests/ui/consts/const-eval/auxiliary/stability.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Crate that exports a const fn. Used for testing cross-crate.

#![crate_type="rlib"]
#![stable(feature = "rust1", since = "1.0.0")]

#![feature(staged_api)]

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_unstable(feature="foo", issue = "none")]
pub const fn foo() -> u32 { 42 }


