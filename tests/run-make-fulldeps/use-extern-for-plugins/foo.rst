tests/run-make-fulldeps/use-extern-for-plugins/foo.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![crate_type = "lib"]
#![crate_name = "a"]

#[macro_export]
macro_rules! foo {
    () => ()
}


