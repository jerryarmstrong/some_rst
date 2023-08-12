tests/ui/generator/generator-resume-after-panic.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// needs-unwind
// error-pattern:generator resumed after panicking
// ignore-emscripten no processes

// Test that we get the correct message for resuming a panicked generator.

#![feature(generators, generator_trait)]

use std::{
    ops::Generator,
    pin::Pin,
    panic,
};

fn main() {
    let mut g = || {
        panic!();
        yield;
    };
    panic::catch_unwind(panic::AssertUnwindSafe(|| {
        let x = Pin::new(&mut g).resume(());
    }));
    Pin::new(&mut g).resume(());
}


