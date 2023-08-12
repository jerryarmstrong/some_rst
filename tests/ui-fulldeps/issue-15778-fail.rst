tests/ui-fulldeps/issue-15778-fail.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-for-crate.rs
// ignore-stage1
// compile-flags: -D crate-not-okay

#![feature(plugin)] //~ ERROR crate is not marked with #![crate_okay]
#![plugin(lint_for_crate)]
//~^ WARN use of deprecated attribute `plugin`

pub fn main() { }


