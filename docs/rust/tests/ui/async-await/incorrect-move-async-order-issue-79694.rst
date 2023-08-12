tests/ui/async-await/incorrect-move-async-order-issue-79694.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// edition:2018

// Regression test for issue 79694

fn main() {
    let _ = move async { }; //~ ERROR 7:13: 7:23: the order of `move` and `async` is incorrect
}


