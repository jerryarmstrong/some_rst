src/tools/clippy/clippy_lints/src/methods/chars_last_cmp_with_unwrap.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::methods::chars_cmp_with_unwrap;
use rustc_lint::LateContext;

use super::CHARS_LAST_CMP;

/// Checks for the `CHARS_LAST_CMP` lint with `unwrap()`.
pub(super) fn check(cx: &LateContext<'_>, info: &crate::methods::BinaryExprInfo<'_>) -> bool {
    if chars_cmp_with_unwrap::check(cx, info, &["chars", "last", "unwrap"], CHARS_LAST_CMP, "ends_with") {
        true
    } else {
        chars_cmp_with_unwrap::check(cx, info, &["chars", "next_back", "unwrap"], CHARS_LAST_CMP, "ends_with")
    }
}


