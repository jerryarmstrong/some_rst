src/tools/rustfmt/tests/source/associated_type_bounds.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See #3657 - https://github.com/rust-lang/rustfmt/issues/3657

#![feature(associated_type_bounds)]

fn f<I: Iterator<Item: Clone>>() {}

fn g<I: Iterator<Item : Clone>>() {}

fn h<I: Iterator<Item :      Clone>>() {}

fn i<I: Iterator<Item:Clone>>() {}

fn j<I: Iterator<Item :  Clone+'a>>() {}


