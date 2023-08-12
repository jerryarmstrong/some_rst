tests/run-make-fulldeps/cdylib-dylib-linkage/foo.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

extern crate bar;

#[no_mangle]
pub extern "C" fn foo() {
    bar::bar();
}

#[no_mangle]
pub extern "C" fn bar(a: u32, b: u32) -> u32 {
    a + b
}


