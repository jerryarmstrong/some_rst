src/tools/clippy/clippy_lints/src/unit_types/utils.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_hir::{Expr, ExprKind};

pub(super) fn is_unit_literal(expr: &Expr<'_>) -> bool {
    matches!(expr.kind, ExprKind::Tup(slice) if slice.is_empty())
}


