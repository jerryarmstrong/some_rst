src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/unimplemented_builtin_macro.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::{Diagnostic, DiagnosticsContext, Severity};

// Diagnostic: unimplemented-builtin-macro
//
// This diagnostic is shown for builtin macros which are not yet implemented by rust-analyzer
pub(crate) fn unimplemented_builtin_macro(
    ctx: &DiagnosticsContext<'_>,
    d: &hir::UnimplementedBuiltinMacro,
) -> Diagnostic {
    Diagnostic::new(
        "unimplemented-builtin-macro",
        "unimplemented built-in macro".to_string(),
        ctx.sema.diagnostics_display_range(d.node.clone()).range,
    )
    .severity(Severity::WeakWarning)
}


