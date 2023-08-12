tests/ui/proc-macro/attr-args.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:attr-args.rs

#![allow(warnings)]

extern crate attr_args;
use attr_args::{attr_with_args, identity};

#[attr_with_args(text = "Hello, world!")]
fn foo() {}

#[identity(fn main() { assert_eq!(foo(), "Hello, world!"); })]
struct Dummy;


