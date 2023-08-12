tests/ui/parser/issues/issue-7970b.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

macro_rules! test {}
//~^ ERROR unexpected end of macro invocation


