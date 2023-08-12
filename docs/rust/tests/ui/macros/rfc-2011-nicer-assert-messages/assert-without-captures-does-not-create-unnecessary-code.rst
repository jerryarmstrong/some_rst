tests/ui/macros/rfc-2011-nicer-assert-messages/assert-without-captures-does-not-create-unnecessary-code.rs
==========================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:common.rs
// only-x86_64
// run-pass
// needs-unwind Asserting on contents of error message

#![feature(core_intrinsics, generic_assert, generic_assert_internals)]

extern crate common;

fn main() {
  common::test!(
    let mut _nothing = ();
    [ 1 == 3 ] => "Assertion failed: 1 == 3"
  );
}


