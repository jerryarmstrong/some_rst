library/std/src/os/wasi/io/fd.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Owned and borrowed file descriptors.

#![unstable(feature = "wasi_ext", issue = "71213")]

// Tests for this module
#[cfg(test)]
mod tests;

pub use crate::os::fd::owned::*;


