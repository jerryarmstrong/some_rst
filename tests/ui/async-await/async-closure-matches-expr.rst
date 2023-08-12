tests/ui/async-await/async-closure-matches-expr.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// edition:2018

#![feature(async_closure)]

macro_rules! match_expr {
    ($x:expr) => {}
}

fn main() {
    match_expr!(async || {});
}


