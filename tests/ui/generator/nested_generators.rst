tests/ui/generator/nested_generators.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators, generator_trait)]

use std::ops::{Generator, GeneratorState};
use std::pin::Pin;

fn main() {
    let _generator = || {
        let mut sub_generator = || {
            yield 2;
        };

        match Pin::new(&mut sub_generator).resume(()) {
            GeneratorState::Yielded(x) => {
                yield x;
            }
            _ => panic!(),
        };
    };
}


