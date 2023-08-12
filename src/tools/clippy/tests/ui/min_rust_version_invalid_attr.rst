src/tools/clippy/tests/ui/min_rust_version_invalid_attr.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(custom_inner_attributes)]
#![clippy::msrv = "invalid.version"]

fn main() {}

#[clippy::msrv = "invalid.version"]
fn outer_attr() {}

mod multiple {
    #![clippy::msrv = "1.40"]
    #![clippy::msrv = "=1.35.0"]
    #![clippy::msrv = "1.10.1"]

    mod foo {
        #![clippy::msrv = "1"]
        #![clippy::msrv = "1.0.0"]
    }
}


