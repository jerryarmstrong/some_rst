tests/ui/lint/empty-lint-attributes.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lint_reasons)]

// check-pass

// Empty (and reason-only) lint attributes are legal—although we may want to
// lint them in the future (Issue #55112).

#![allow()]
#![warn(reason = "observationalism")]

#[forbid()]
fn devoir() {}

#[deny(reason = "ultion")]
fn waldgrave() {}

fn main() {}


