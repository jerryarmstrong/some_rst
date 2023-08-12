tests/ui/rfc-2627-raw-dylib/import-name-type-invalid-format.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
// only-x86
#![feature(raw_dylib)]

#[link(name = "foo", kind = "raw-dylib", import_name_type = 6)]
//~^ ERROR import name type must be of the form `import_name_type = "string"`
extern "C" { }

fn main() {}


