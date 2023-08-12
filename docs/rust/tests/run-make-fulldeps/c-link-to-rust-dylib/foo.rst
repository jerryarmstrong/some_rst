tests/run-make-fulldeps/c-link-to-rust-dylib/foo.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]

#[no_mangle]
pub extern "C" fn foo() {}


