tests/run-make/wasm-export-all-symbols/bar.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[no_mangle]
pub extern fn foo() {}

#[no_mangle]
pub static FOO: u64 = 42;


