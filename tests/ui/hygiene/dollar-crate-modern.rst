tests/ui/hygiene/dollar-crate-modern.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure `$crate` and `crate` work in for basic cases of nested macros.

// check-pass
// aux-build:intercrate.rs

#![feature(decl_macro)]

extern crate intercrate;

// `$crate`
intercrate::uses_dollar_crate_modern!();

intercrate::define_uses_dollar_crate_modern_nested!(uses_dollar_crate_modern_nested);
uses_dollar_crate_modern_nested!();

intercrate::define_uses_dollar_crate_legacy_nested!();
uses_dollar_crate_legacy_nested!();

// `crate`
intercrate::uses_crate_modern!();

intercrate::define_uses_crate_modern_nested!(uses_crate_modern_nested);
uses_crate_modern_nested!();

fn main() {}


