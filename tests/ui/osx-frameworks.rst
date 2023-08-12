tests/ui/osx-frameworks.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-macos this is supposed to succeed on osx

#[link(name = "foo", kind = "framework")]
extern "C" {}
//~^^ ERROR: link kind `framework` is only supported on Apple targets

fn main() {}


