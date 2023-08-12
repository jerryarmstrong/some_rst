tests/ui/lint/rfc-2383-lint-reason/expect_with_reason.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(lint_reasons)]
#![warn(unused)]

#![expect(unused_variables, reason = "<This should fail and display this reason>")]
//~^ WARNING this lint expectation is unfulfilled [unfulfilled_lint_expectations]
//~| NOTE `#[warn(unfulfilled_lint_expectations)]` on by default
//~| NOTE <This should fail and display this reason>

fn main() {}


