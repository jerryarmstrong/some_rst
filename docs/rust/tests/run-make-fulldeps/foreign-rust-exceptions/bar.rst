tests/run-make-fulldeps/foreign-rust-exceptions/bar.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]
#![feature(c_unwind)]

#[no_mangle]
extern "C-unwind" fn panic() {
    panic!();
}


