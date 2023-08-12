tests/ui/proc-macro/attributes-included.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:attributes-included.rs
// check-pass

#![warn(unused)]

extern crate attributes_included;

use attributes_included::*;

#[bar]
#[inline]
/// doc
#[foo]
#[inline]
/// doc
fn foo() {
    let a: i32 = "foo"; //~ WARN: unused variable
}

fn main() {
    foo()
}


