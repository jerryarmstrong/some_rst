tests/ui/async-await/issues/issue-54752-async-block.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// edition:2018
// pp-exact

fn main() { let _a = (async { }); }
//~^ WARNING unnecessary parentheses around assigned value


