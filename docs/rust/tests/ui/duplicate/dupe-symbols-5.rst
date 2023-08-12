tests/ui/duplicate/dupe-symbols-5.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

//
#![crate_type="rlib"]
#![allow(warnings)]

#[export_name="fail"]
static HELLO: u8 = 0;

#[export_name="fail"]
pub fn b() {
//~^ symbol `fail` is already defined
}


