tests/ui/dyn-keyword/dyn-angle-brackets.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See https://github.com/rust-lang/rust/issues/88508
// run-rustfix
// edition:2018
#![deny(bare_trait_objects)]
#![allow(dead_code)]
#![allow(unused_imports)]

use std::fmt;

#[derive(Debug)]
pub struct Foo;

impl fmt::Display for Foo {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        <fmt::Debug>::fmt(self, f)
        //~^ ERROR trait objects without an explicit `dyn` are deprecated
        //~| WARNING this is accepted in the current edition
    }
}

fn main() {}


