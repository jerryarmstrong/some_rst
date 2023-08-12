tests/ui/lint/rfc-2383-lint-reason/expect_on_fn_params.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(lint_reasons)]

#[warn(unused_variables)]

/// This should catch the unused_variables lint and not emit anything
fn check_fulfilled_expectation(#[expect(unused_variables)] unused_value: u32) {}

fn check_unfulfilled_expectation(#[expect(unused_variables)] used_value: u32) {
    //~^ WARNING this lint expectation is unfulfilled [unfulfilled_lint_expectations]
    //~| NOTE `#[warn(unfulfilled_lint_expectations)]` on by default
    println!("I use the value {used_value}");
}

fn main() {}


