tests/ui/lint/lint-expr-stmt-attrs-for-early-lints.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(stmt_expr_attributes)]
#![deny(unused_parens)]

// Tests that lint attributes on statements/expressions are
// correctly applied to non-builtin early (AST) lints

fn main() {
    #[allow(unused_parens)]
    {
        let _ = (9);
    }
}


