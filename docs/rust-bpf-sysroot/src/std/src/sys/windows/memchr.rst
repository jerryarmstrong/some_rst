src/std/src/sys/windows/memchr.rs
=================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    // Original implementation taken from rust-memchr.
// Copyright 2015 Andrew Gallant, bluss and Nicolas Koch

// Fallback memchr is fastest on Windows.
pub use core::slice::memchr::{memchr, memrchr};


