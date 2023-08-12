tests/ui/generator/generator-region-requirements.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]
use std::ops::{Generator, GeneratorState};
use std::pin::Pin;

fn dangle(x: &mut i32) -> &'static mut i32 {
    let mut g = || {
        yield;
        x
    };
    loop {
        match Pin::new(&mut g).resume(()) {
            GeneratorState::Complete(c) => return c,
            //~^ ERROR lifetime may not live long enough
            GeneratorState::Yielded(_) => (),
        }
    }
}

fn main() {}


