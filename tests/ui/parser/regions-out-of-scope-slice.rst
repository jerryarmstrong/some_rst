tests/ui/parser/regions-out-of-scope-slice.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This basically tests the parser's recovery on `'blk` in the wrong place.

fn foo(cond: bool) {
    let mut x;

    if cond {
        x = &'blk [1,2,3]; //~ ERROR borrow expressions cannot be annotated with lifetimes
    }
}

fn main() {}


