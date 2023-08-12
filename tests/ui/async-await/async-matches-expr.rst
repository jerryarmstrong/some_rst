tests/ui/async-await/async-matches-expr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

macro_rules! match_expr {
    ($x:expr) => {}
}

fn main() {
    match_expr!(async {});
}


