tests/run-make/rustc-macro-dep-files/bar.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![crate_type = "lib"]

#[macro_use]
extern crate foo;

#[derive(A)]
struct A;


