tests/ui/expr/if/if-typeck.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:mismatched types
// issue #513

fn f() { }

fn main() {

    // f is not a bool
    if f { }
}


