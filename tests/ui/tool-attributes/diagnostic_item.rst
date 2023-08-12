tests/ui/tool-attributes/diagnostic_item.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[rustc_diagnostic_item = "foomp"] //~ ERROR compiler internal support for linting
struct Foomp;
fn main() {}


