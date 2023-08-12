tests/run-make/env-dep-info/macro_def.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(proc_macro_tracked_env)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn access_env_vars(_: TokenStream) -> TokenStream {
    let _ = tracked_env::var("EXISTING_PROC_MACRO_ENV");
    let _ = tracked_env::var("NONEXISTENT_PROC_MACEO_ENV");
    TokenStream::new()
}


