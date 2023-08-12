tests/ui/lint/unused/unused-macro-with-follow-violation.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

macro_rules! test {
    ($e:expr +) => () //~ ERROR not allowed for `expr` fragments
}

fn main() { }


