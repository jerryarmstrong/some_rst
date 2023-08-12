tests/run-make-fulldeps/static-dylib-by-default/bar.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]

extern crate foo;

#[no_mangle]
pub extern "C" fn bar() {
    foo::foo();
}


