tests/pretty/trait-polarity.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

// pp-exact

struct Test;

impl !Send for Test {}

pub fn main() {}


