tests/ui/tool-attributes/diagnostic_item3.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(rustc_attrs)]

#[rustc_diagnostic_item = "foomp"]
struct Foomp;

fn main() {}


