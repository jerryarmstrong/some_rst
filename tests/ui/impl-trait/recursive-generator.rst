tests/ui/impl-trait/recursive-generator.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

use std::ops::{Generator, GeneratorState};

fn foo() -> impl Generator<Yield = (), Return = ()> {
    //~^ ERROR cannot resolve opaque type
    //~| NOTE recursive opaque type
    //~| NOTE in this expansion of desugaring of
    || {
    //~^ NOTE returning here
        let mut gen = Box::pin(foo());
        //~^ NOTE generator captures itself here
        let mut r = gen.as_mut().resume(());
        while let GeneratorState::Yielded(v) = r {
            yield v;
            r = gen.as_mut().resume(());
        }
    }
}

fn main() {
    foo();
}


