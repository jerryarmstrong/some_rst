tests/ui/errors/remap-path-prefix.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --remap-path-prefix={{src-base}}=remapped
// no-remap-src-base: Manually remap, so the remapped path remains in .stderr file.

// The remapped paths are not normalized by compiletest.
// normalize-stderr-test: "\\(errors)" -> "/$1"

// The remapped paths aren't recognized by compiletest, so we
// cannot use line-specific patterns.
// error-pattern: E0425

fn main() {
    // We cannot actually put an ERROR marker here because
    // the file name in the error message is not what the
    // test framework expects (since the filename gets remapped).
    // We still test the expected error in the stderr file.
    ferris
}


