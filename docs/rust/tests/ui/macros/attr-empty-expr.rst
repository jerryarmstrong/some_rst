tests/ui/macros/attr-empty-expr.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // AST-based macro attributes expanding to an empty expression produce an error and not ICE.

#![feature(custom_test_frameworks)]
#![feature(stmt_expr_attributes)]
#![feature(test)]

fn main() {
    let _ = #[test] 0; //~ ERROR removing an expression is not supported in this position
    let _ = #[bench] 1; //~ ERROR removing an expression is not supported in this position
    let _ = #[test_case] 2; //~ ERROR removing an expression is not supported in this position
}


