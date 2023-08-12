tests/ui/ffi_pure.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ffi_pure)]
#![crate_type = "lib"]

#[ffi_pure] //~ ERROR `#[ffi_pure]` may only be used on foreign functions
pub fn foo() {}


