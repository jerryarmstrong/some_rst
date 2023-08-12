tests/ui/output-type-mismatch.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: mismatched types

fn f() { }

fn main() { let i: isize; i = f(); }


