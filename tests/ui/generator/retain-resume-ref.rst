tests/ui/generator/retain-resume-ref.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This test ensures that a mutable reference cannot be passed as a resume argument twice.

#![feature(generators, generator_trait)]

use std::marker::Unpin;
use std::ops::{
    Generator,
    GeneratorState::{self, *},
};
use std::pin::Pin;

fn main() {
    let mut thing = String::from("hello");

    let mut gen = |r| {
        if false {
            yield r;
        }
    };

    let mut gen = Pin::new(&mut gen);
    gen.as_mut().resume(&mut thing);
    gen.as_mut().resume(&mut thing);
    //~^ cannot borrow `thing` as mutable more than once at a time
}


