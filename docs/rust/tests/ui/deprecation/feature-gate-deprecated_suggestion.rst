tests/ui/deprecation/feature-gate-deprecated_suggestion.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

#![no_implicit_prelude]

#[deprecated(suggestion = "foo")] //~ ERROR suggestions on deprecated items are unstable
struct Foo {}


