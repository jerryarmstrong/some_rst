tests/ui/lint/must_not_suspend/other_items.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![feature(must_not_suspend)]
#![deny(must_not_suspend)]

#[must_not_suspend] //~ ERROR attribute should be
mod inner {}

fn main() {}


