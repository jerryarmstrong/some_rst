tests/ui/generator/yield-subtype.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(dead_code)]

#![feature(generators)]

fn bar<'a>() {
    let a: &'static str = "hi";
    let b: &'a str = a;

    || { //~ WARN unused generator that must be used
        yield a;
        yield b;
    };
}

fn main() {}


