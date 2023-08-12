tests/ui/lint/lint-malformed.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny = "foo"] //~ ERROR malformed `deny` attribute input
#![allow(bar = "baz")] //~ ERROR malformed lint attribute
                       //~| ERROR malformed lint attribute
                       //~| ERROR malformed lint attribute
                       //~| ERROR malformed lint attribute
fn main() { }


