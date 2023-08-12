tests/ui/malformed/malformed-plugin-1.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(plugin)]
#![plugin] //~ ERROR malformed `plugin` attribute
//~| WARN use of deprecated attribute `plugin`: compiler plugins are deprecated

fn main() {}


