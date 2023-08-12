tests/run-make-fulldeps/mingw-export-call-convention/foo.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

#[no_mangle]
pub extern "system" fn bar() {}


