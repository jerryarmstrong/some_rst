tests/ui/privacy/privacy-reexport.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:privacy_reexport.rs

// pretty-expanded FIXME #23616

extern crate privacy_reexport;

pub fn main() {
    // Check that public extern crates are visible to outside crates
    privacy_reexport::core::cell::Cell::new(0);

    privacy_reexport::bar::frob();
}


