tests/run-make/wasm-import-module/foo.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![deny(warnings)]

#[link(wasm_import_module = "./dep")]
extern "C" {
    pub fn dep();
}


