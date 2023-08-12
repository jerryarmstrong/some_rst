tests/ui/attributes/attr-before-view-item.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// pretty-expanded FIXME #23616

#![feature(rustc_attrs)]
#![feature(test)]

#[rustc_dummy = "bar"]
extern crate test;

fn main() {}


