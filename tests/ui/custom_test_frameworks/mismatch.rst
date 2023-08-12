tests/ui/custom_test_frameworks/mismatch.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:example_runner.rs
// compile-flags:--test
#![feature(custom_test_frameworks)]
#![test_runner(example_runner::runner)]

extern crate example_runner;

#[test]
fn wrong_kind(){}
//~^ ERROR trait bound `TestDescAndFn: Testable` is not satisfied


