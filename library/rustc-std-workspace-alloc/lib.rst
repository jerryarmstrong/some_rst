library/rustc-std-workspace-alloc/lib.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_core)]
#![no_core]

// See rustc-std-workspace-core for why this crate is needed.

// Rename the crate to avoid conflicting with the alloc module in alloc.
extern crate alloc as foo;

pub use foo::*;


