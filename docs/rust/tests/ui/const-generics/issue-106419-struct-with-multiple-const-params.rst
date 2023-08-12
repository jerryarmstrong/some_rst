tests/ui/const-generics/issue-106419-struct-with-multiple-const-params.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

#[derive(Clone)]
struct Bar<const A: usize, const B: usize>
where
    [(); A as usize]:,
    [(); B as usize]:,
{}

fn main() {}


