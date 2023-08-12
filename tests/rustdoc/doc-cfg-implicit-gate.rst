tests/rustdoc/doc-cfg-implicit-gate.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--cfg feature="worricow"
#![crate_name = "xenogenous"]

// @has 'xenogenous/struct.Worricow.html'
// @count   - '//*[@class="stab portability"]' 0
#[cfg(feature = "worricow")]
pub struct Worricow;


