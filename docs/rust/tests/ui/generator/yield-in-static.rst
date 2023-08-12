tests/ui/generator/yield-in-static.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

static B: u8 = { yield 3u8; 3u8};
//~^ ERROR yield expression outside

fn main() {}


