tests/ui/deprecation/deprecation-lint-3.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:deprecation-lint.rs
// error-pattern: use of deprecated function

#![deny(deprecated)]
#![allow(warnings)]

#[macro_use]
extern crate deprecation_lint;

use deprecation_lint::*;

fn main() {
    macro_test_arg_nested!(deprecated_text);
}


