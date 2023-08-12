tests/ui/generator/xcrate.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// aux-build:xcrate.rs

#![feature(generators, generator_trait)]

extern crate xcrate;

use std::ops::{GeneratorState, Generator};
use std::pin::Pin;

fn main() {
    let mut foo = xcrate::foo();

    match Pin::new(&mut foo).resume(()) {
        GeneratorState::Complete(()) => {}
        s => panic!("bad state: {:?}", s),
    }

    let mut foo = xcrate::bar(3);

    match Pin::new(&mut foo).resume(()) {
        GeneratorState::Yielded(3) => {}
        s => panic!("bad state: {:?}", s),
    }
    match Pin::new(&mut foo).resume(()) {
        GeneratorState::Complete(()) => {}
        s => panic!("bad state: {:?}", s),
    }
}


