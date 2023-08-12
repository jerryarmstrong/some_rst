tests/ui/attributes/unrestricted-attribute-tokens.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![feature(rustc_attrs)]

#[rustc_dummy(a b c d)]
#[rustc_dummy[a b c d]]
#[rustc_dummy{a b c d}]
fn main() {}


