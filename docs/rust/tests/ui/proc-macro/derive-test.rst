tests/ui/proc-macro/derive-test.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// no-prefer-dynamic
// compile-flags: --test

#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::TokenStream;

// ```
// assert!(true);
// ```
#[proc_macro_derive(Foo)]
pub fn derive_foo(_input: TokenStream) -> TokenStream {
    "".parse().unwrap()
}

#[test]
pub fn test_derive() {
    assert!(true);
}


