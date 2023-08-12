tests/rustdoc/doc-proc-macro.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #52129: ICE when trying to document the `quote` proc-macro from proc_macro

// As of this writing, we don't currently attempt to document proc-macros. However, we shouldn't
// crash when we try.

extern crate proc_macro;

pub use proc_macro::*;


