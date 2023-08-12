tests/rustdoc-ui/wasm-safe.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[cfg(any(target_arch = "wasm32", doc))]
#[target_feature(enable = "simd128")]
pub fn foo() {}


