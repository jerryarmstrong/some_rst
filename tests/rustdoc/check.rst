tests/rustdoc/check.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options --check

// @!has check/fn.foo.html
// @!has check/index.html
pub fn foo() {}


