tests/rustdoc/duplicate-flags.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items --document-private-items

// @has duplicate_flags/struct.Private.html
struct Private;


