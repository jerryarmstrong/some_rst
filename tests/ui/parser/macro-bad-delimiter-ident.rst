tests/ui/parser/macro-bad-delimiter-ident.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    foo! bar < //~ ERROR expected one of `(`, `[`, or `{`, found `bar`
}


