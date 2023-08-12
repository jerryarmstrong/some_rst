tests/run-make-fulldeps/cross-lang-lto/lib.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn foo() {
    println!("abc");
}


