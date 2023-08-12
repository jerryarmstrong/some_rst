tests/ui/deprecation/deprecated-macro_escape.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[macro_escape] //~ WARNING `#[macro_escape]` is a deprecated synonym for `#[macro_use]`
mod foo {}

fn main() {}


