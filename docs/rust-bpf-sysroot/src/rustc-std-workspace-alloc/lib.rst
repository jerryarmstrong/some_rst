src/rustc-std-workspace-alloc/lib.rs
====================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![feature(no_core)]
#![no_core]

// See rustc-std-workspace-core for why this crate is needed.

// Rename the crate to avoid conflicting with the alloc module in liballoc.
extern crate alloc as foo;

pub use foo::*;


