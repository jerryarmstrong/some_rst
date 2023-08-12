tests/ui/lint/unaligned_references_external_macro.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:unaligned_references_external_crate.rs

extern crate unaligned_references_external_crate;

unaligned_references_external_crate::mac! { //~ERROR reference to packed field is unaligned
    //~^ previously accepted
    #[repr(packed)]
    pub struct X {
        pub field: u16
    }
}

fn main() {}


