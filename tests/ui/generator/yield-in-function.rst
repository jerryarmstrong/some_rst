tests/ui/generator/yield-in-function.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn main() { yield; }
//~^ ERROR yield expression outside


