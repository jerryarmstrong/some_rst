tests/ui/generator/resume-after-return.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind


#![feature(generators, generator_trait)]

use std::ops::{GeneratorState, Generator};
use std::pin::Pin;
use std::panic;

fn main() {
    let mut foo = || {
        if true {
            return
        }
        yield;
    };

    match Pin::new(&mut foo).resume(()) {
        GeneratorState::Complete(()) => {}
        s => panic!("bad state: {:?}", s),
    }

    match panic::catch_unwind(move || Pin::new(&mut foo).resume(())) {
        Ok(_) => panic!("generator successfully resumed"),
        Err(_) => {}
    }
}


