tests/ui/lint/rfc-2383-lint-reason/crate_level_expect.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(lint_reasons)]

#![warn(unused)]

#![expect(unused_mut)]
//~^ WARNING this lint expectation is unfulfilled [unfulfilled_lint_expectations]
//~| NOTE `#[warn(unfulfilled_lint_expectations)]` on by default

#![expect(unused_variables)]

fn main() {
    let x = 0;
}


