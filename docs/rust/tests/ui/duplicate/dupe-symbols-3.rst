tests/ui/duplicate/dupe-symbols-3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

//
#![crate_type="rlib"]
#![allow(warnings)]

#[export_name="fail"]
pub fn a() {
}

#[no_mangle]
pub fn fail() {
//~^ symbol `fail` is already defined
}


