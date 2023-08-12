tests/ui-fulldeps/auxiliary/empty-plugin.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host

#![feature(rustc_private)]

extern crate rustc_driver;
use rustc_driver::plugin::Registry;

#[no_mangle]
fn __rustc_plugin_registrar(_: &mut Registry) {}


