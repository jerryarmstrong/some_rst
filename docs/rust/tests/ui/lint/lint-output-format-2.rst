tests/ui/lint/lint-output-format-2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint_output_format.rs

#![feature(unstable_test_feature)]
// check-pass

extern crate lint_output_format;
use lint_output_format::{foo, bar};
//~^ WARNING use of deprecated function `lint_output_format::foo`: text


fn main() {
    let _x = foo();
    //~^ WARNING use of deprecated function `lint_output_format::foo`: text
    let _y = bar();
}


