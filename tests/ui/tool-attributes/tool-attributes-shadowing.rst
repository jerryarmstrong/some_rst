tests/ui/tool-attributes/tool-attributes-shadowing.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod rustfmt {}

#[rustfmt::skip] //~ ERROR failed to resolve: could not find `skip` in `rustfmt`
fn main() {}


