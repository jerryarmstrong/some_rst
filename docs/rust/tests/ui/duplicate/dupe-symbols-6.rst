tests/ui/duplicate/dupe-symbols-6.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![crate_type="rlib"]
#![allow(warnings)]

#[export_name="fail"]
static HELLO: u8 = 0;

#[export_name="fail"]
static HELLO_TWICE: u16 = 0;
//~^ symbol `fail` is already defined


