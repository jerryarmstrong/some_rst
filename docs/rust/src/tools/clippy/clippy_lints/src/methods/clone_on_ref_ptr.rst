src/tools/clippy/clippy_lints/src/methods/clone_on_ref_ptr.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy_utils::diagnostics::span_lint_and_sugg;
use clippy_utils::paths;
use clippy_utils::source::snippet_with_macro_callsite;
use clippy_utils::ty::{is_type_diagnostic_item, match_type};
use rustc_errors::Applicability;
use rustc_hir as hir;
use rustc_lint::LateContext;
use rustc_middle::ty;
use rustc_span::symbol::{sym, Symbol};

use super::CLONE_ON_REF_PTR;

pub(super) fn check(
    cx: &LateContext<'_>,
    expr: &hir::Expr<'_>,
    method_name: Symbol,
    receiver: &hir::Expr<'_>,
    args: &[hir::Expr<'_>],
) {
    if !(args.is_empty() && method_name == sym::clone) {
        return;
    }
    let obj_ty = cx.typeck_results().expr_ty(receiver).peel_refs();

    if let ty::Adt(_, subst) = obj_ty.kind() {
        let caller_type = if is_type_diagnostic_item(cx, obj_ty, sym::Rc) {
            "Rc"
        } else if is_type_diagnostic_item(cx, obj_ty, sym::Arc) {
            "Arc"
        } else if match_type(cx, obj_ty, &paths::WEAK_RC) || match_type(cx, obj_ty, &paths::WEAK_ARC) {
            "Weak"
        } else {
            return;
        };

        let snippet = snippet_with_macro_callsite(cx, receiver.span, "..");

        span_lint_and_sugg(
            cx,
            CLONE_ON_REF_PTR,
            expr.span,
            "using `.clone()` on a ref-counted pointer",
            "try this",
            format!("{caller_type}::<{}>::clone(&{snippet})", subst.type_at(0)),
            Applicability::Unspecified, // Sometimes unnecessary ::<_> after Rc/Arc/Weak
        );
    }
}


