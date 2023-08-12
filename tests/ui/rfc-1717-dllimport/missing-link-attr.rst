tests/ui/rfc-1717-dllimport/missing-link-attr.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -l foo:bar
// error-pattern: renaming of the library `foo` was specified

#![crate_type = "lib"]


