tests/ui-fulldeps/deriving-encodable-decodable-cell-refcell.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
// This briefly tests the capability of `Cell` and `RefCell` to implement the
// `Encodable` and `Decodable` traits via `#[derive(Encodable, Decodable)]`
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
use std::cell::{Cell, RefCell};

#[derive(Encodable, Decodable)]
struct A {
    baz: isize,
}

#[derive(Encodable, Decodable)]
struct B {
    foo: Cell<bool>,
    bar: RefCell<A>,
}

fn main() {
    let obj = B { foo: Cell::new(true), bar: RefCell::new(A { baz: 2 }) };

    let mut encoder = MemEncoder::new();
    obj.encode(&mut encoder);
    let data = encoder.finish();

    let mut decoder = MemDecoder::new(&data, 0);
    let obj2 = B::decode(&mut decoder);

    assert_eq!(obj.foo.get(), obj2.foo.get());
    assert_eq!(obj.bar.borrow().baz, obj2.bar.borrow().baz);
}


