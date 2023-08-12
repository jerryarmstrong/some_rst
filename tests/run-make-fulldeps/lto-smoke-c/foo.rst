tests/run-make-fulldeps/lto-smoke-c/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "staticlib"]

#[no_mangle]
pub extern "C" fn foo() {}


