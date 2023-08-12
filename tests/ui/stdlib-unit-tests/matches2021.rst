tests/ui/stdlib-unit-tests/matches2021.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// edition:2021

// regression test for https://github.com/rust-lang/rust/pull/85678

#![feature(assert_matches)]

use std::assert_matches::assert_matches;

fn main() {
    assert!(matches!((), ()));
    assert_matches!((), ());
}


