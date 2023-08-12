tests/ui/range/range_traits-7.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

use std::ops::*;

#[derive(Copy, Clone)]
struct R(RangeToInclusive<usize>);


fn main() {}


