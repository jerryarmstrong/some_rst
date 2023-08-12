tests/run-make-fulldeps/issue-14500/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn foo() {}

#[no_mangle]
pub static FOO_STATIC: u8 = 0;


