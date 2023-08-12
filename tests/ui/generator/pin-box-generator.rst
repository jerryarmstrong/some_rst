tests/ui/generator/pin-box-generator.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators, generator_trait)]

use std::ops::Generator;

fn assert_generator<G: Generator>(_: G) {
}

fn main() {
    assert_generator(static || yield);
    assert_generator(Box::pin(static || yield));
}


