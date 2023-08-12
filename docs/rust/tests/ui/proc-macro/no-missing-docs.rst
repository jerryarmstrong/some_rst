tests/ui/proc-macro/no-missing-docs.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Verify that the `decls` module implicitly added by the compiler does not cause `missing_docs`
//! warnings.

// build-pass (FIXME(62277): could be check-pass?)
// force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]
#![deny(missing_docs)]

extern crate proc_macro;
use proc_macro::*;

/// Foo1.
#[proc_macro]
pub fn foo1(input: TokenStream) -> TokenStream { input }


