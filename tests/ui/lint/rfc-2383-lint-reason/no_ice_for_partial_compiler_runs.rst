tests/ui/lint/rfc-2383-lint-reason/no_ice_for_partial_compiler_runs.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This ensures that ICEs like rust#94953 don't happen
// check-pass
// compile-flags: -Z unpretty=expanded

#![feature(lint_reasons)]

// This `expect` will create an expectation with an unstable expectation id
#[expect(while_true)]
fn create_early_lint_pass_expectation() {
    // `while_true` is an early lint
    while true {}
}

fn main() {
    create_early_lint_pass_expectation();
}


