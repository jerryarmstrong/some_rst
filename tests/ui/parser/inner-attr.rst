tests/ui/parser/inner-attr.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[feature(lang_items)]

#![recursion_limit="100"] //~ ERROR an inner attribute is not permitted following an outer attribute
fn main() {}


