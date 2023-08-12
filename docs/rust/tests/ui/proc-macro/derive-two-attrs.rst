tests/ui/proc-macro/derive-two-attrs.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// aux-build:derive-two-attrs.rs

extern crate derive_two_attrs as foo;

use foo::A;

#[derive(A)]
#[b]
#[b]
struct B;

fn main() {}


