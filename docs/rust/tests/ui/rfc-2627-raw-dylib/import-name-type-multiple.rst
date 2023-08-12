tests/ui/rfc-2627-raw-dylib/import-name-type-multiple.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength
// only-windows
// only-x86
#![feature(raw_dylib)]

#[link(name = "foo", kind = "raw-dylib", import_name_type = "decorated", import_name_type = "decorated")]
//~^ ERROR multiple `import_name_type` arguments in a single `#[link]` attribute
extern "C" { }

fn main() {}


