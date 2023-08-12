tests/ui/tail-typeck.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: mismatched types

fn f() -> isize { return g(); }

fn g() -> usize { return 0; }

fn main() { let y = f(); }


