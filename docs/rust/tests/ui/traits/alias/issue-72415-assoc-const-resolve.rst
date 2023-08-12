tests/ui/traits/alias/issue-72415-assoc-const-resolve.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(trait_alias)]

trait Bounded { const MAX: Self; }

impl Bounded for u32 {
    // This should correctly resolve to the associated const in the inherent impl of u32.
    const MAX: Self = u32::MAX;
}

trait Num = Bounded + Copy;

fn main() {}


