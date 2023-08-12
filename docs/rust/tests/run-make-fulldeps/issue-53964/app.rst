tests/run-make-fulldeps/issue-53964/app.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "bin"]
#![no_main]
#![no_std]

#![deny(unused_extern_crates)]

// `panic` provides a `panic_handler` so it shouldn't trip the `unused_extern_crates` lint
extern crate panic;


