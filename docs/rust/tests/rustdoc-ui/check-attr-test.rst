tests/rustdoc-ui/check-attr-test.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test

#![deny(rustdoc::invalid_codeblock_attributes)]

/// foo
///
/// ```compile-fail,compilefail,comPile_fail
/// boo
/// ```
pub fn foo() {}

/// bar
///
/// ```should-panic,shouldpanic,shOuld_panic
/// boo
/// ```
pub fn bar() {}

/// foobar
///
/// ```no-run,norun,nO_run
/// boo
/// ```
pub fn foobar() {}

/// b
///
/// ```test-harness,testharness,tesT_harness
/// boo
/// ```
pub fn b() {}


