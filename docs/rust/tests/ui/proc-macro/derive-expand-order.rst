tests/ui/proc-macro/derive-expand-order.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:multiple-derives.rs

extern crate multiple_derives;

use multiple_derives::*;

#[derive(First)]
#[derive(Second)]
#[derive(Third, Fourth)]
#[derive(Fifth)]
pub struct Foo {}

fn main() {}


