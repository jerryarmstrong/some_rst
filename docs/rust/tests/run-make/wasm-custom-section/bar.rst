tests/run-make/wasm-custom-section/bar.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]
#![deny(warnings)]

extern crate foo;

#[link_section = "foo"]
pub static A: [u8; 2] = [5, 6];

#[link_section = "baz"]
pub static B: [u8; 2] = [7, 8];

#[no_mangle]
pub extern fn foo() {}


