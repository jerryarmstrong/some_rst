tests/run-make/track-path-dep-info/macro_def.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(track_path)]
#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn access_tracked_paths(_: TokenStream) -> TokenStream {
    tracked_path::path("emojis.txt");
    TokenStream::new()
}


