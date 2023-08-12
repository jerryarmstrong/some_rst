tests/ui/lint/rfc-2383-lint-reason/multiple_expect_attrs.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(lint_reasons)]
#![warn(unused)]

#[warn(unused_variables)]
#[expect(unused_variables)]
//~^ WARNING this lint expectation is unfulfilled [unfulfilled_lint_expectations]
//~| NOTE `#[warn(unfulfilled_lint_expectations)]` on by default
#[allow(unused_variables)]
#[expect(unused_variables)] // Only this expectation will be fulfilled
fn main() {
    let x = 2;
}


