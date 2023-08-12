tests/ui/expr/if/attrs/bad-cfg.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(stmt_expr_attributes)]

fn main() {
    let _ = #[cfg(FALSE)] if true {}; //~ ERROR removing an expression
}


