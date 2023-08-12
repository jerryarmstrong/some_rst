tests/ui/proc-macro/issue-76182-leading-vert-pat.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:test-macros.rs
// compile-flags: -Z span-debug
//
// Regression test for issue #76182
// Tests that we properly handle patterns with a leading vert

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

extern crate test_macros;

#[test_macros::print_attr]
fn main() {
    match () { | () => () }
}


