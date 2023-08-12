tests/ui/macros/local-ambiguity-multiple-parsing-options.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

macro_rules! ambiguity {
    ($($i:ident)* $j:ident) => {};
}

ambiguity!(error); //~ ERROR local ambiguity
ambiguity!(error); //~ ERROR local ambiguity


