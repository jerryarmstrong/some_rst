tests/ui/proc-macro/auxiliary/gen-macro-rules-hygiene.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]

extern crate proc_macro;
use proc_macro::*;

#[proc_macro]
pub fn gen_macro_rules(_: TokenStream) -> TokenStream {
    "
    macro_rules! generated {() => {
        struct ItemDef;
        let local_def = 0;

        ItemUse; // OK
        local_use; // ERROR
        break 'label_use; // ERROR

        type DollarCrate = $crate::ItemUse; // OK
    }}
    ".parse().unwrap()
}


