tests/ui/hygiene/assoc_item_ctxt.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-pretty pretty-printing is unhygienic

#![feature(decl_macro)]
#![allow(unused)]

mod ok {
    macro mac_trait_item($method: ident) {
        fn $method();
    }

    trait Tr {
        mac_trait_item!(method);
    }

    macro mac_trait_impl() {
        impl Tr for u8 { // OK
            fn method() {} // OK
        }
    }

    mac_trait_impl!();
}

mod error {
    macro mac_trait_item() {
        fn method();
    }

    trait Tr {
        mac_trait_item!();
    }

    macro mac_trait_impl() {
        impl Tr for u8 { //~ ERROR not all trait items implemented, missing: `method`
            fn method() {} //~ ERROR method `method` is not a member of trait `Tr`
        }
    }

    mac_trait_impl!();
}

fn main() {}


