tests/pretty/fn-return.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

// Check that `fn f() -> () {}` does not print as `fn f() {}`.

fn f() -> () {}

fn main() {}


