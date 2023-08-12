tests/ui/json/json-options.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// ignore-pass (different metadata emitted in different modes)
// compile-flags: --json=diagnostic-short,artifacts --error-format=json

#![crate_type = "lib"]


