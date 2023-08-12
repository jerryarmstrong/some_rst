tests/rustdoc/decl_macro_priv.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items

#![feature(decl_macro)]

// @has decl_macro_priv/macro.crate_macro.html //pre 'pub(crate) macro crate_macro() {'
// @has - //pre '...'
// @has - //pre '}'
pub(crate) macro crate_macro() {}

// @has decl_macro_priv/macro.priv_macro.html //pre 'macro priv_macro() {'
// @!has - //pre 'pub macro priv_macro() {'
// @has - //pre '...'
// @has - //pre '}'
macro priv_macro() {}


