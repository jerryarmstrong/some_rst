tests/ui/rfc-2627-raw-dylib/import-name-type-unsupported-link-kind.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
// only-x86
#![feature(raw_dylib)]

#[link(name = "foo", import_name_type = "decorated")]
//~^ ERROR import name type can only be used with link kind `raw-dylib`
extern "C" { }

#[link(name = "bar", kind = "static", import_name_type = "decorated")]
//~^ ERROR import name type can only be used with link kind `raw-dylib`
extern "C" { }

// Specifying `import_name_type` before `kind` shouldn't raise an error.
#[link(name = "bar", import_name_type = "decorated", kind = "raw-dylib")]
extern "C" { }

fn main() {}


