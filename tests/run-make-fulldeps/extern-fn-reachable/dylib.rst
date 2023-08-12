tests/run-make-fulldeps/extern-fn-reachable/dylib.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]
#![allow(dead_code)]

#[no_mangle] pub extern "C" fn fun1() {}
#[no_mangle] extern "C" fn fun2() {}

mod foo {
    #[no_mangle] pub extern "C" fn fun3() {}
}
pub mod bar {
    #[no_mangle] pub extern "C" fn fun4() {}
}

#[no_mangle] pub fn fun5() {}


