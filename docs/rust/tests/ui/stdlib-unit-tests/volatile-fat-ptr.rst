tests/ui/stdlib-unit-tests/volatile-fat-ptr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(stable_features)]
#![feature(volatile)]
use std::ptr::{read_volatile, write_volatile};

fn main() {
    let mut x: &'static str = "test";
    unsafe {
        let a = read_volatile(&x);
        assert_eq!(a, "test");
        write_volatile(&mut x, "foo");
        assert_eq!(x, "foo");
    }
}


