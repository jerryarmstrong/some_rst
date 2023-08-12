tests/ui/rfc-1717-dllimport/rename-modifiers.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -l dylib=foo:bar
// error-pattern: overriding linking modifiers from command line is not supported

#![feature(native_link_modifiers_as_needed)]

#![crate_type = "lib"]

#[link(name = "foo", kind = "dylib", modifiers = "-as-needed")]
extern "C" {}


