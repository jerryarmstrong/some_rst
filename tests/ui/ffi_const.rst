tests/ui/ffi_const.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ffi_const)]
#![crate_type = "lib"]

#[ffi_const] //~ ERROR `#[ffi_const]` may only be used on foreign functions
pub fn foo() {}


