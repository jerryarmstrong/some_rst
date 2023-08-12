tests/run-make/wasm-custom-sections-opt/foo.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]
#![deny(warnings)]

#[link_section = "foo"]
pub static A: [u8; 2] = [1, 2];

// make sure this is in another CGU
pub mod another {
    #[link_section = "foo"]
    pub static FOO: [u8; 2] = [3, 4];

    pub fn foo() {}
}

#[no_mangle]
pub extern fn foo() {
    // This will import `another::foo` through ThinLTO passes, and it better not
    // also accidentally import the `FOO` custom section into this module as
    // well
    another::foo();
}


