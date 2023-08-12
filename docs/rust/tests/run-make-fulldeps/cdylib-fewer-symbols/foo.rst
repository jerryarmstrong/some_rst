tests/run-make-fulldeps/cdylib-fewer-symbols/foo.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

#[no_mangle]
pub extern "C" fn foo() -> u32 {
    3
}


