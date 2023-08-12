src/tools/clippy/tests/ui/crashes/trivial_bounds.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trivial_bounds)]
#![allow(unused, trivial_bounds)]

fn test_trivial_bounds()
where
    i32: Iterator,
{
    for _ in 2i32 {}
}

fn main() {}


