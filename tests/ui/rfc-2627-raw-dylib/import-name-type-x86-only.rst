tests/ui/rfc-2627-raw-dylib/import-name-type-x86-only.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
// ignore-x86
#[link(name = "foo", kind = "raw-dylib", import_name_type = "decorated")]
//~^ ERROR import name type is only supported on x86
extern "C" { }

fn main() {}


