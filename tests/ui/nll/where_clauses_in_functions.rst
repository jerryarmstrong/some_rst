tests/ui/nll/where_clauses_in_functions.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

fn foo<'a, 'b>(x: &'a u32, y: &'b u32) -> (&'a u32, &'b u32)
where
    'a: 'b,
{
    (x, y)
}

fn bar<'a, 'b>(x: &'a u32, y: &'b u32) -> (&'a u32, &'b u32) {
    foo(x, y)
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


