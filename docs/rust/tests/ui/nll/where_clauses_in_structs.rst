tests/ui/nll/where_clauses_in_structs.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::cell::Cell;

struct Foo<'a: 'b, 'b> {
    x: Cell<&'a u32>,
    y: Cell<&'b u32>,
}

fn bar<'a, 'b>(x: Cell<&'a u32>, y: Cell<&'b u32>) {
    Foo { x, y };
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


