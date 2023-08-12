tests/run-make/wasm-symbols-different-module/foo.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

mod a {
    #[link(wasm_import_module = "a")]
    extern "C" {
        pub fn foo();
    }
}

mod b {
    #[link(wasm_import_module = "b")]
    extern "C" {
        pub fn foo();
    }
}

#[no_mangle]
pub fn start() {
    unsafe {
        a::foo();
        b::foo();
    }
}


