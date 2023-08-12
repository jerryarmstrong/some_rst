tests/run-make-fulldeps/staticlib-blank-lib/foo.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "staticlib"]

#[link(name = "foo", kind = "static")]
extern "C" {}

fn main() {}


