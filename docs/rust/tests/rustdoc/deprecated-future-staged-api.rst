tests/rustdoc/deprecated-future-staged-api.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "deprecated-future-staged-api", since = "1.0.0")]

// @has deprecated_future_staged_api/index.html '//*[@class="stab deprecated"]' \
//      'Deprecation planned'
// @has deprecated_future_staged_api/struct.S1.html '//*[@class="stab deprecated"]' \
//      'Deprecating in 99.99.99: effectively never'
#[deprecated(since = "99.99.99", note = "effectively never")]
#[stable(feature = "deprecated-future-staged-api", since = "1.0.0")]
pub struct S1;

// @has deprecated_future_staged_api/index.html '//*[@class="stab deprecated"]' \
//      'Deprecation planned'
// @has deprecated_future_staged_api/struct.S2.html '//*[@class="stab deprecated"]' \
//      'Deprecating in a future Rust version: literally never'
#[deprecated(since = "TBD", note = "literally never")]
#[stable(feature = "deprecated-future-staged-api", since = "1.0.0")]
pub struct S2;


