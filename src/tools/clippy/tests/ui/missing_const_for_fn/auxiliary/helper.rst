src/tools/clippy/tests/ui/missing_const_for_fn/auxiliary/helper.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file provides a const function that is unstably const forever.

#![feature(staged_api)]
#![stable(feature = "1", since = "1.0.0")]

#[stable(feature = "1", since = "1.0.0")]
#[rustc_const_unstable(feature = "foo", issue = "none")]
pub const fn unstably_const_fn() {}


