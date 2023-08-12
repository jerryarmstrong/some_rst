tests/ui/ffi_returns_twice.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ffi_returns_twice)]
#![crate_type = "lib"]

#[ffi_returns_twice] //~ ERROR `#[ffi_returns_twice]` may only be used on foreign functions
pub fn foo() {}


