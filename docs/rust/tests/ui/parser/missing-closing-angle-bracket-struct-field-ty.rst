tests/ui/parser/missing-closing-angle-bracket-struct-field-ty.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustifx
#![allow(unused)]
use std::sync::{Arc, Mutex};

pub struct Foo {
    a: Mutex<usize>,
    b: Arc<Mutex<usize>, //~ HELP you might have meant to end the type parameters here
    c: Arc<Mutex<usize>>,
} //~ ERROR expected one of

fn main() {}


