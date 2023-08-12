tests/run-make-fulldeps/use-extern-for-plugins/bar.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_core)]
#![no_core]
#![crate_type = "lib"]
#![crate_name = "a"]

#[macro_export]
macro_rules! bar {
    () => ()
}


