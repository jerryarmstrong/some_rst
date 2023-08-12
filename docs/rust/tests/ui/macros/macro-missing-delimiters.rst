tests/ui/macros/macro-missing-delimiters.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! baz(
    baz => () //~ ERROR invalid macro matcher;
);

fn main() {
    baz!(baz);
}


