src/tools/clippy/clippy_lints/src/methods/chars_next_cmp_with_unwrap.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_lint::LateContext;

use super::CHARS_NEXT_CMP;

/// Checks for the `CHARS_NEXT_CMP` lint with `unwrap()`.
pub(super) fn check(cx: &LateContext<'_>, info: &crate::methods::BinaryExprInfo<'_>) -> bool {
    crate::methods::chars_cmp_with_unwrap::check(cx, info, &["chars", "next", "unwrap"], CHARS_NEXT_CMP, "starts_with")
}


