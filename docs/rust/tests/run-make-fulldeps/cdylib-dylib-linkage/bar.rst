tests/run-make-fulldeps/cdylib-dylib-linkage/bar.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]

pub fn bar() {
    println!("hello!");
}


