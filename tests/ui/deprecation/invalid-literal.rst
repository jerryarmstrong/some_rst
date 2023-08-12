tests/ui/deprecation/invalid-literal.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deprecated = b"test"] //~ ERROR malformed `deprecated` attribute
fn foo() {}

fn main() {}


