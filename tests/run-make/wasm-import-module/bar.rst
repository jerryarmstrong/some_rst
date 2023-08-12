tests/run-make/wasm-import-module/bar.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]
#![deny(warnings)]

extern crate foo;

#[link(wasm_import_module = "./me")]
extern "C" {
    #[link_name = "me_in_dep"]
    fn dep();
}

#[no_mangle]
pub extern "C" fn foo() {
    unsafe {
        foo::dep();
        dep();
    }
}


