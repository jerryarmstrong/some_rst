tests/ui/test-attrs/test-warns-dead-code.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test

#![deny(dead_code)]

fn dead() {} //~ error: function `dead` is never used

fn main() {}


