tests/ui-fulldeps/deriving-encodable-decodable-box.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
#![feature(rustc_private)]

extern crate rustc_macros;
extern crate rustc_serialize;

// Necessary to pull in object code as the rest of the rustc crates are shipped only as rmeta
// files.
#[allow(unused_extern_crates)]
extern crate rustc_driver;

use rustc_macros::{Decodable, Encodable};
use rustc_serialize::opaque::{MemDecoder, MemEncoder};
use rustc_serialize::{Decodable, Encodable, Encoder};

#[derive(Encodable, Decodable)]
struct A {
    foo: Box<[bool]>,
}

fn main() {
    let obj = A { foo: Box::new([true, false]) };

    let mut encoder = MemEncoder::new();
    obj.encode(&mut encoder);
    let data = encoder.finish();

    let mut decoder = MemDecoder::new(&data, 0);
    let obj2 = A::decode(&mut decoder);

    assert_eq!(obj.foo, obj2.foo);
}


