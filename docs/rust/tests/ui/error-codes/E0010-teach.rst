tests/ui/error-codes/E0010-teach.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z teach

#![feature(box_syntax)]
#![allow(warnings)]

const CON : Box<i32> = box 0; //~ ERROR E0010

fn main() {}


