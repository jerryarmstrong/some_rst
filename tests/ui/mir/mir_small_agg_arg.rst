tests/ui/mir/mir_small_agg_arg.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
fn foo((x, y): (i8, i8)) {
}

fn main() {
    foo((0, 1));
}


