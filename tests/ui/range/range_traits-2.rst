tests/ui/range/range_traits-2.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::*;

#[derive(Copy, Clone)] //~ ERROR Copy
struct R(Range<usize>);

fn main() {}


