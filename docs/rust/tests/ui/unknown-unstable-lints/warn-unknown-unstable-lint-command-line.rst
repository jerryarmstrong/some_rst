tests/ui/unknown-unstable-lints/warn-unknown-unstable-lint-command-line.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Wunknown_lints -Atest_unstable_lint
// error-pattern: unknown lint: `test_unstable_lint`
// error-pattern: the `test_unstable_lint` lint is unstable

fn main() {}


