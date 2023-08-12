tests/ui/cross-crate/xcrate-trait-lifetime-param.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:xcrate-trait-lifetime-param.rs

// pretty-expanded FIXME #23616

extern crate xcrate_trait_lifetime_param as other;

struct Reader<'a> {
    b : &'a [u8]
}

impl <'a> other::FromBuf<'a> for Reader<'a> {
    fn from_buf(b : &'a [u8]) -> Reader<'a> {
        Reader { b : b }
    }
}

pub fn main () {}


