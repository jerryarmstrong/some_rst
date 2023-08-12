tests/ui/feature-gates/feature-gate-no_core.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#![no_core] //~ ERROR the `#[no_core]` attribute is an experimental feature

pub struct S {}


