src/tools/clippy/clippy_lints/src/permissions_set_readonly_false.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy_utils::diagnostics::span_lint_and_then;
use clippy_utils::paths;
use clippy_utils::ty::match_type;
use rustc_ast::ast::LitKind;
use rustc_hir::{Expr, ExprKind};
use rustc_lint::{LateContext, LateLintPass};
use rustc_session::{declare_lint_pass, declare_tool_lint};

declare_clippy_lint! {
    /// ### What it does
    /// Checks for calls to `std::fs::Permissions.set_readonly` with argument `false`.
    ///
    /// ### Why is this bad?
    /// On Unix platforms this results in the file being world writable,
    /// equivalent to `chmod a+w <file>`.
    /// ### Example
    /// ```rust
    /// use std::fs::File;
    /// let f = File::create("foo.txt").unwrap();
    /// let metadata = f.metadata().unwrap();
    /// let mut permissions = metadata.permissions();
    /// permissions.set_readonly(false);
    /// ```
    #[clippy::version = "1.66.0"]
    pub PERMISSIONS_SET_READONLY_FALSE,
    suspicious,
    "Checks for calls to `std::fs::Permissions.set_readonly` with argument `false`"
}
declare_lint_pass!(PermissionsSetReadonlyFalse => [PERMISSIONS_SET_READONLY_FALSE]);

impl<'tcx> LateLintPass<'tcx> for PermissionsSetReadonlyFalse {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx Expr<'tcx>) {
        if let ExprKind::MethodCall(path, receiver, [arg], _) = &expr.kind
            && match_type(cx, cx.typeck_results().expr_ty(receiver), &paths::PERMISSIONS)
            && path.ident.name == sym!(set_readonly)
            && let ExprKind::Lit(lit) = &arg.kind
            && LitKind::Bool(false) == lit.node
        {
            span_lint_and_then(
                cx,
                PERMISSIONS_SET_READONLY_FALSE,
                expr.span,
                "call to `set_readonly` with argument `false`",
                |diag| {
                    diag.note("on Unix platforms this results in the file being world writable");
                    diag.help("you can set the desired permissions using `PermissionsExt`. For more information, see\n\
                        https://doc.rust-lang.org/std/os/unix/fs/trait.PermissionsExt.html");
                }
            );
        }
    }
}


