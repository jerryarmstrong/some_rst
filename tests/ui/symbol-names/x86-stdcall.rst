tests/ui/symbol-names/x86-stdcall.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// only-x86-windows
#![crate_type = "cdylib"]
#![feature(abi_vectorcall)]

#[no_mangle]
extern "stdcall" fn foo(_: bool) {}

#[no_mangle]
extern "fastcall" fn bar(_: u8) {}

#[no_mangle]
extern "vectorcall" fn baz(_: u16) {}


