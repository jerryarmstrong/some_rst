src/tools/clippy/clippy_lints/src/misc_early/redundant_pattern.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use clippy_utils::diagnostics::span_lint_and_sugg;
use rustc_ast::ast::{Pat, PatKind};
use rustc_errors::Applicability;
use rustc_lint::EarlyContext;

use super::REDUNDANT_PATTERN;

pub(super) fn check(cx: &EarlyContext<'_>, pat: &Pat) {
    if let PatKind::Ident(ann, ident, Some(ref right)) = pat.kind {
        if let PatKind::Wild = right.kind {
            span_lint_and_sugg(
                cx,
                REDUNDANT_PATTERN,
                pat.span,
                &format!(
                    "the `{} @ _` pattern can be written as just `{}`",
                    ident.name, ident.name,
                ),
                "try",
                format!("{}{}", ann.prefix_str(), ident.name),
                Applicability::MachineApplicable,
            );
        }
    }
}


