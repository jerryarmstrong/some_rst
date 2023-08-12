tests/testsuite/mock-std/library/test/src/lib.rs
================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![feature(test)]
#![unstable(feature = "test", issue = "none")]

extern crate test;

pub use test::*;

pub fn custom_api() {
}


