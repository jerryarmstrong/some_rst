tests/ui/parser/attribute-with-no-generics-in-parameter-list.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<#[attr]>() {} //~ ERROR attribute without generic parameters

fn main() {}


