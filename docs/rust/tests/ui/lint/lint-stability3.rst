tests/ui/lint/lint-stability3.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint_stability.rs
// error-pattern: use of deprecated function

#![deny(deprecated)]
#![allow(warnings)]

#[macro_use]
extern crate lint_stability;

use lint_stability::*;

fn main() {
    macro_test_arg_nested!(deprecated_text);
}


