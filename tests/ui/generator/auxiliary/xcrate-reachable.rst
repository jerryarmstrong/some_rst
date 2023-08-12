tests/ui/generator/auxiliary/xcrate-reachable.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

use std::ops::Generator;

fn msg() -> u32 {
    0
}

pub fn foo() -> impl Generator<(), Yield=(), Return=u32> {
    || {
        yield;
        return msg();
    }
}


