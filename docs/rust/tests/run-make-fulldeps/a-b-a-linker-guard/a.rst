tests/run-make-fulldeps/a-b-a-linker-guard/a.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "a"]
#![crate_type = "dylib"]

#[cfg(x)]
pub fn foo(x: u32) { }

#[cfg(y)]
pub fn foo(x: i32) { }


