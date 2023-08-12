tests/rustdoc-ui/generate-link-to-definition-opt.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test purpose is to check that the "--generate-link-to-definition"
// option can only be used with HTML generation.

// compile-flags: -Zunstable-options --generate-link-to-definition --output-format json

pub fn f() {}


