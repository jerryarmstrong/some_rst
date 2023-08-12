tests/run-make-fulldeps/panic-impl-transitive/panic-impl-consumer.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![no_main]

// this crate provides the `panic_impl` lang item so we don't need to define it here
extern crate panic_impl_provider;


