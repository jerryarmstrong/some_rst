tests/ui/foreign/foreign-mod-unused-const.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

mod foo {
    extern "C" {
        pub static errno: u32;
    }
}

pub fn main() {}


