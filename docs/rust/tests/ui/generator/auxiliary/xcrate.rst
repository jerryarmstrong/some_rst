tests/ui/generator/auxiliary/xcrate.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

use std::marker::Unpin;
use std::ops::Generator;

pub fn foo() -> impl Generator<(), Yield = (), Return = ()> {
    || {
        if false {
            yield;
        }
    }
}

pub fn bar<T: 'static>(t: T) -> Box<Generator<(), Yield = T, Return = ()> + Unpin> {
    Box::new(|| {
        yield t;
    })
}


