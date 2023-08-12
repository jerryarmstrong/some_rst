tests/ui-fulldeps/plugin-as-extern-crate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:empty-plugin.rs
// ignore-cross-compile
//
// empty_plugin will not compile on a cross-compiled target because
// librustc_ast is not compiled for it.

extern crate empty_plugin; // OK, plugin crates are still crates

fn main() {}


