tests/ui/no-core-1.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(stable_features)]
#![feature(no_core, core)]
#![no_core]

extern crate std;
extern crate core;

use std::option::Option::Some;

fn main() {
    let a = Some("foo");
    a.unwrap();
}


