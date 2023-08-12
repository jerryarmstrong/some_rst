tests/ui/rfc-1717-dllimport/rename-to-empty.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -l foo:
// error-pattern: an empty renaming target was specified for library

#![crate_type = "lib"]

#[link(name = "foo")]
extern "C" {}


