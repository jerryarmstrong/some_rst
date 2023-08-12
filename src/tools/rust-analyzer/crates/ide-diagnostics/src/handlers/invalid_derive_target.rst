src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/invalid_derive_target.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::{Diagnostic, DiagnosticsContext, Severity};

// Diagnostic: invalid-derive-target
//
// This diagnostic is shown when the derive attribute is used on an item other than a `struct`,
// `enum` or `union`.
pub(crate) fn invalid_derive_target(
    ctx: &DiagnosticsContext<'_>,
    d: &hir::InvalidDeriveTarget,
) -> Diagnostic {
    let display_range = ctx.sema.diagnostics_display_range(d.node.clone()).range;

    Diagnostic::new(
        "invalid-derive-target",
        "`derive` may only be applied to `struct`s, `enum`s and `union`s",
        display_range,
    )
    .severity(Severity::Error)
}

#[cfg(test)]
mod tests {
    use crate::tests::check_diagnostics;

    #[test]
    fn fails_on_function() {
        check_diagnostics(
            r#"
//- minicore:derive
mod __ {
    #[derive()]
  //^^^^^^^^^^^ error: `derive` may only be applied to `struct`s, `enum`s and `union`s
    fn main() {}
}
            "#,
        );
    }
}


