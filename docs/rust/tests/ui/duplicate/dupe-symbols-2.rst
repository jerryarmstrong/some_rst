tests/ui/duplicate/dupe-symbols-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

//
#![crate_type="rlib"]
#![allow(warnings)]

pub mod a {
    #[no_mangle]
    pub extern "C" fn fail() {
    }
}

pub mod b {
    #[no_mangle]
    pub extern "C" fn fail() {
    //~^ symbol `fail` is already defined
    }
}


