tests/ui/parser/attr.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lang_items)]

fn main() {}

#![lang = "foo"] //~ ERROR an inner attribute is not permitted in this context
fn foo() {}


