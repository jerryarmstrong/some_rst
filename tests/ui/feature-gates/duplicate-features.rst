tests/ui/feature-gates/duplicate-features.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(stable_features)]

#![feature(rust1)]
#![feature(rust1)] //~ ERROR the feature `rust1` has already been declared

#![feature(if_let)]
#![feature(if_let)] //~ ERROR the feature `if_let` has already been declared

fn main() {}


