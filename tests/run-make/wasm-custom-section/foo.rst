tests/run-make/wasm-custom-section/foo.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![deny(warnings)]

#[link_section = "foo"]
pub static A: [u8; 2] = [1, 2];

#[link_section = "bar"]
pub static B: [u8; 2] = [3, 4];


