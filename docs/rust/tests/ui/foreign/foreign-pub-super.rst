tests/ui/foreign/foreign-pub-super.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for #79487
// check-pass

#![allow(dead_code)]

mod sha2 {
    extern "C" {
        pub(super) fn GFp_sha512_block_data_order();
    }
}

fn main() {}


