tests/ui/test-attrs/test-cant-be-shadowed.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:test_macro.rs
// compile-flags:--test

#[macro_use] extern crate test_macro;

#[test]
fn foo(){}

macro_rules! test { () => () }

#[test]
fn bar() {}


