tests/pretty/gat-bounds.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that associated types print generic parameters and where clauses.
// See issue #67509.

// pretty-compare-only

trait X {
    type Y<T>: Trait where Self: Sized;
}

impl X for () {
    type Y<T> where Self: Sized = u32;
}

fn f<T: X<Y<()> = i32>>() {}

fn main() { }


