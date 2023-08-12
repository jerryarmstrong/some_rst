tests/testsuite/mock-std/library/alloc/src/lib.rs
=================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(since = "1.0.0", feature = "dummy")]

extern crate alloc;

#[stable(since = "1.0.0", feature = "dummy")]
pub use alloc::*;

#[stable(since = "1.0.0", feature = "dummy")]
pub fn custom_api() {
}


