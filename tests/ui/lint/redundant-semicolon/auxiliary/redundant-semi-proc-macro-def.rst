tests/ui/lint/redundant-semicolon/auxiliary/redundant-semi-proc-macro-def.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic
#![crate_type="proc-macro"]
#![crate_name="redundant_semi_proc_macro"]
extern crate proc_macro;
use proc_macro::TokenStream;

#[proc_macro_attribute]
pub fn should_preserve_spans(_attr: TokenStream, item: TokenStream) -> TokenStream {
    eprintln!("{:?}", item);
    item
}


