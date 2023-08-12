tests/ui/wrong-ret-type.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: mismatched types
fn mk_int() -> usize { let i: isize = 3; return i; }
fn main() { }


