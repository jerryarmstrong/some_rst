tests/ui/crate-name-mismatch.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-name foo

#![crate_name = "bar"]
//~^ ERROR: `--crate-name` and `#[crate_name]` are required to match, but `foo` != `bar`

fn main() {}


