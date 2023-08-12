tests/ui-fulldeps/rustc_encodable_hygiene.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(rustc_private)]

extern crate rustc_macros;
#[allow(dead_code)]
extern crate rustc_serialize;

// Necessary to pull in object code as the rest of the rustc crates are shipped only as rmeta
// files.
#[allow(unused_extern_crates)]
extern crate rustc_driver;

use rustc_macros::{Decodable, Encodable};

#[derive(Decodable, Encodable, Debug)]
struct A {
    a: String,
}

trait Trait {
    fn encode(&self);
}

impl<T> Trait for T {
    fn encode(&self) {
        unimplemented!()
    }
}

fn main() {}


