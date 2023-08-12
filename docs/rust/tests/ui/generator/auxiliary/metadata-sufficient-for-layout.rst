tests/ui/generator/auxiliary/metadata-sufficient-for-layout.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit metadata
#![feature(generators, generator_trait)]

use std::marker::Unpin;
use std::ops::Generator;

pub fn g() -> impl Generator<(), Yield = (), Return = ()> {
    || {
        yield;
    }
}


