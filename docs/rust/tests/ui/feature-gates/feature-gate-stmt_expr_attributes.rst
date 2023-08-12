tests/ui/feature-gates/feature-gate-stmt_expr_attributes.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const X: i32 = #[allow(dead_code)] 8;
//~^ ERROR attributes on expressions are experimental

fn main() {}


