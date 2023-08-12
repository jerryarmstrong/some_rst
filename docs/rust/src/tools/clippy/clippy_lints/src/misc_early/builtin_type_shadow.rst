src/tools/clippy/clippy_lints/src/misc_early/builtin_type_shadow.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy_utils::diagnostics::span_lint;
use rustc_ast::ast::{GenericParam, GenericParamKind};
use rustc_hir::PrimTy;
use rustc_lint::EarlyContext;

use super::BUILTIN_TYPE_SHADOW;

pub(super) fn check(cx: &EarlyContext<'_>, param: &GenericParam) {
    if let GenericParamKind::Type { .. } = param.kind {
        if let Some(prim_ty) = PrimTy::from_name(param.ident.name) {
            span_lint(
                cx,
                BUILTIN_TYPE_SHADOW,
                param.ident.span,
                &format!("this generic shadows the built-in type `{}`", prim_ty.name()),
            );
        }
    }
}


