tests/rustdoc-ui/check-attr.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::invalid_codeblock_attributes)]

/// foo
//~^ ERROR
//~^^ ERROR
//~^^^ ERROR
///
/// ```compile-fail,compilefail,comPile_fail
/// boo
/// ```
pub fn foo() {}

/// bar
//~^ ERROR
//~^^ ERROR
//~^^^ ERROR
///
/// ```should-panic,shouldpanic,sHould_panic
/// boo
/// ```
pub fn bar() {}

/// foobar
//~^ ERROR
//~^^ ERROR
//~^^^ ERROR
///
/// ```no-run,norun,no_Run
/// boo
/// ```
pub fn foobar() {}

/// b
//~^ ERROR
//~^^ ERROR
//~^^^ ERROR
///
/// ```test-harness,testharness,teSt_harness
/// boo
/// ```
pub fn b() {}


