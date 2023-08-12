tests/run-make-fulldeps/issue-38237/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "proc-macro"]

extern crate proc_macro;

#[proc_macro_derive(A)]
pub fn derive(ts: proc_macro::TokenStream) -> proc_macro::TokenStream { ts }

#[derive(Debug)]
struct S;


