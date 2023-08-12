tests/ui/parser/issues/issue-70552-ascription-in-parens-after-call.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    expr as fun()(:); //~ ERROR expected expression
}


