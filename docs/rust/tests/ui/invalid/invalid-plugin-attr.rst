tests/ui/invalid/invalid-plugin-attr.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_attributes)]
#![feature(plugin)]

#[plugin(bla)] //~ ERROR should be an inner attribute
//~| WARN use of deprecated attribute `plugin`: compiler plugins are deprecated

fn main() {}


