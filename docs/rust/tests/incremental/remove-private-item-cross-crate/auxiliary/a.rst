tests/incremental/remove-private-item-cross-crate/auxiliary/a.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]
#![crate_name = "a"]
#![crate_type = "rlib"]

pub fn foo(b: u8) -> u32 { b as u32 }

#[cfg(rpass1)]
fn bar() { }


