tests/ui/proc-macro/proc-macro-deprecated-attr.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// force-host
// no-prefer-dynamic

#![deny(deprecated)]

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
#[deprecated(since = "1.0.0", note = "test")]
pub fn test_compile_without_warning_with_deprecated(_: TokenStream) -> TokenStream {
    TokenStream::new()
}


