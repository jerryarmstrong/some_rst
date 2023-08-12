tests/ui/feature-gates/feature-gate-decl_macro.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

macro m() {} //~ ERROR `macro` is experimental

fn main() {}


