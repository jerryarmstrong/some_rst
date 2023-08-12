tests/ui/rfc-1717-dllimport/multiple-renames.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -l foo:bar -l foo:baz
// error-pattern: multiple renamings were specified for library

#![crate_type = "lib"]

#[link(name = "foo")]
extern "C" {}


