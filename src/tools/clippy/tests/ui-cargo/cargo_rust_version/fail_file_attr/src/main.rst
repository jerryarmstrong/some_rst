src/tools/clippy/tests/ui-cargo/cargo_rust_version/fail_file_attr/src/main.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME: this should produce a warning, because the attribute says 1.58 and the cargo.toml file
// says 1.13

#![feature(custom_inner_attributes)]
#![clippy::msrv = "1.58.0"]
#![deny(clippy::use_self)]

pub struct Foo;

impl Foo {
    pub fn bar() -> Foo {
        Foo
    }
}

fn main() {}


