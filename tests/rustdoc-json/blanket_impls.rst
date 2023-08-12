tests/rustdoc-json/blanket_impls.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/98658>

#![no_std]

// @has "$.index[*][?(@.name=='Error')].kind" \"assoc_type\"
// @has "$.index[*][?(@.name=='Error')].inner.default.kind" \"resolved_path\"
// @has "$.index[*][?(@.name=='Error')].inner.default.inner.name" \"Infallible\"
pub struct ForBlanketTryFromImpl;


