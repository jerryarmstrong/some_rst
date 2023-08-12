tests/ui/rfc-2627-raw-dylib/import-name-type-unknown-value.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-windows
// only-x86
#![feature(raw_dylib)]

#[link(name = "foo", kind = "raw-dylib", import_name_type = "unknown")]
//~^ ERROR unknown import name type `unknown`, expected one of: decorated, noprefix, undecorated
extern "C" { }

fn main() {}


