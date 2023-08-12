tests/ui/panic-runtime/auxiliary/depends.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![feature(panic_runtime)]
#![crate_type = "rlib"]
#![panic_runtime]
#![no_std]

extern crate needs_panic_runtime;


