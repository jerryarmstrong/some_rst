tests/ui/panic-runtime/auxiliary/needs-panic-runtime.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![feature(needs_panic_runtime)]
#![crate_type = "rlib"]
#![needs_panic_runtime]
#![no_std]


