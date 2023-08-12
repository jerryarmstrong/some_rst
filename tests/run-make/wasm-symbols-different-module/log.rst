tests/run-make/wasm-symbols-different-module/log.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Issue #56309

#![crate_type = "cdylib"]

#[link(wasm_import_module = "test")]
extern "C" {
    fn log(message_data: u32, message_size: u32);
}

#[no_mangle]
pub fn main() {
    let message = "Hello, world!";
    unsafe {
        log(message.as_ptr() as u32, message.len() as u32);
    }
}


