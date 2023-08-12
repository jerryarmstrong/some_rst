tests/pretty/yeet-expr.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact
#![feature(yeet_expr)]

fn yeet_no_expr() -> Option<String> { do yeet }

fn yeet_no_expr_with_semicolon() -> Option<String> { do yeet; }

fn yeet_with_expr() -> Result<String, i32> { do yeet 1 + 2 }

fn yeet_with_expr_with_semicolon() -> Result<String, i32> { do yeet 1 + 2; }

fn main() {}


