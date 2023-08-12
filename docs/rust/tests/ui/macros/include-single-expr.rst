tests/ui/macros/include-single-expr.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern include macro expected single expression

fn main() {
    include!("include-single-expr-helper.rs");
    include!("include-single-expr-helper-1.rs");
}


