tests/ui/proc-macro/dollar-crate-issue-101211.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021
// aux-build:test-macros.rs

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

macro_rules! foo {
    ($($path:ident)::*) => (
        test_macros::recollect!(
            $($path)::*
        )
    )
}

macro_rules! baz {
    () => (
        foo!($crate::BAR)
    )
}

pub const BAR: u32 = 19;

fn main(){
    std::println!("{}", baz!());
}


