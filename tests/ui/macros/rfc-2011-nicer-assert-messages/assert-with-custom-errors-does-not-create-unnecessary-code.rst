tests/ui/macros/rfc-2011-nicer-assert-messages/assert-with-custom-errors-does-not-create-unnecessary-code.rs
============================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test
// run-pass

#![feature(core_intrinsics, generic_assert, generic_assert_internals)]

#[should_panic(expected = "Custom user message")]
#[test]
fn test() {
  assert!(1 == 3, "Custom user message");
}

fn main() {
}


