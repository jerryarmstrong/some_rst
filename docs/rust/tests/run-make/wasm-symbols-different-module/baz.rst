tests/run-make/wasm-symbols-different-module/baz.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Issue #63562

#![crate_type = "cdylib"]

mod foo {
    #[link(wasm_import_module = "sqlite")]
    extern "C" {
        pub fn allocate(size: usize) -> i32;
        pub fn deallocate(ptr: i32, size: usize);
    }
}

#[no_mangle]
pub extern "C" fn allocate() {
    unsafe {
        foo::allocate(1);
        foo::deallocate(1, 2);
    }
}

#[no_mangle]
pub extern "C" fn deallocate() {}


