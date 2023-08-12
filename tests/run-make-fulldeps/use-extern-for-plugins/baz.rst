tests/run-make-fulldeps/use-extern-for-plugins/baz.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_core)]
#![no_core]
#![crate_type = "lib"]

#[macro_use]
extern crate a;

bar!();


