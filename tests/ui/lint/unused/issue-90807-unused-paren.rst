tests/ui/lint/unused/issue-90807-unused-paren.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Make sure unused parens lint doesn't emit a false positive.
// See https://github.com/rust-lang/rust/issues/90807
#![deny(unused_parens)]

fn main() {
    for _ in (1..{ 2 }) {}
}


