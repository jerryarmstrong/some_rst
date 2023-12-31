src/tools/clippy/clippy_lints/src/operators/needless_bitwise_bool.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy_utils::diagnostics::span_lint_and_then;
use clippy_utils::source::snippet_opt;
use rustc_errors::Applicability;
use rustc_hir::{BinOpKind, Expr, ExprKind};
use rustc_lint::LateContext;

use super::NEEDLESS_BITWISE_BOOL;

pub(super) fn check(cx: &LateContext<'_>, e: &Expr<'_>, op: BinOpKind, lhs: &Expr<'_>, rhs: &Expr<'_>) {
    let op_str = match op {
        BinOpKind::BitAnd => "&&",
        BinOpKind::BitOr => "||",
        _ => return,
    };
    if matches!(
        rhs.kind,
        ExprKind::Call(..) | ExprKind::MethodCall(..) | ExprKind::Binary(..) | ExprKind::Unary(..)
    ) && cx.typeck_results().expr_ty(e).is_bool()
        && !rhs.can_have_side_effects()
    {
        span_lint_and_then(
            cx,
            NEEDLESS_BITWISE_BOOL,
            e.span,
            "use of bitwise operator instead of lazy operator between booleans",
            |diag| {
                if let Some(lhs_snip) = snippet_opt(cx, lhs.span)
                    && let Some(rhs_snip) = snippet_opt(cx, rhs.span)
                {
                    let sugg = format!("{lhs_snip} {op_str} {rhs_snip}");
                    diag.span_suggestion(e.span, "try", sugg, Applicability::MachineApplicable);
                }
            },
        );
    }
}


