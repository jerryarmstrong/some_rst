compiler/rustc_mir_build/src/thir/mod.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! The MIR is built from some typed high-level IR
//! (THIR). This section defines the THIR along with a trait for
//! accessing it. The intention is to allow MIR construction to be
//! unit-tested and separated from the Rust source and compiler data
//! structures.

pub(crate) mod constant;

pub(crate) mod cx;

pub(crate) mod pattern;

mod util;


