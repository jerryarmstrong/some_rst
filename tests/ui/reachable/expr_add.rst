tests/ui/reachable/expr_add.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![allow(unused_variables)]
#![deny(unreachable_code)]

use std::ops;

struct Foo;

impl ops::Add<!> for Foo {
    type Output = !;
    fn add(self, rhs: !) -> ! {
        unimplemented!()
    }
}

fn main() {
    let x = Foo + return; //~ ERROR unreachable
}


