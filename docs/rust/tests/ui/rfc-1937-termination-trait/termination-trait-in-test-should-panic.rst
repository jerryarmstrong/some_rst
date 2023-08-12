tests/ui/rfc-1937-termination-trait/termination-trait-in-test-should-panic.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test

#![feature(test)]

extern crate test;
use std::num::ParseIntError;
use test::Bencher;

#[test]
#[should_panic]
fn not_a_num() -> Result<(), ParseIntError> {
    //~^ ERROR functions using `#[should_panic]` must return `()`
    let _: u32 = "abc".parse()?;
    Ok(())
}


