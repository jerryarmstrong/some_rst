tests/ui/macros/macro-def-site-super.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `super` in a `macro` refers to the parent module of the macro itself and not its reexport.

// check-pass
// aux-build:macro-def-site-super.rs

extern crate macro_def_site_super;

type A = macro_def_site_super::public::mac!();

fn main() {}


