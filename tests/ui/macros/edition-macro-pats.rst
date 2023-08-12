tests/ui/macros/edition-macro-pats.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// edition:2021

macro_rules! foo {
    (a $x:pat_param) => {};
    (b $x:pat) => {};
}

fn main() {
    foo!(a None);
    foo!(b 1 | 2);
}


