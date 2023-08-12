tests/ui/wasm-custom-section-relocations.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-wasm32

#[link_section = "test"]
pub static A: &[u8] = &[1]; //~ ERROR: no extra levels of indirection

#[link_section = "test"]
pub static B: [u8; 3] = [1, 2, 3];

#[link_section = "test"]
pub static C: usize = 3;

#[link_section = "test"]
pub static D: &usize = &C; //~ ERROR: no extra levels of indirection

fn main() {}


