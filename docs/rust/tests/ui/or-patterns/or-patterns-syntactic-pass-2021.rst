tests/ui/or-patterns/or-patterns-syntactic-pass-2021.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that :pat in macros in edition 2021 allows top-level or-patterns.

// run-pass
// edition:2021

macro_rules! accept_pat {
    ($p:pat) => {};
}

accept_pat!(p | q);

fn main() {}


