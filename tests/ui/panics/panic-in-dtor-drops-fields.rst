tests/ui/panics/panic-in-dtor-drops-fields.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind
#![allow(dead_code)]
#![allow(non_upper_case_globals)]

// ignore-emscripten no threads support

use std::thread;

static mut dropped: bool = false;

struct A {
    b: B,
}

struct B {
    foo: isize,
}

impl Drop for A {
    fn drop(&mut self) {
        panic!()
    }
}

impl Drop for B {
    fn drop(&mut self) {
        unsafe { dropped = true; }
    }
}

pub fn main() {
    let ret = thread::spawn(move|| {
        let _a = A { b: B { foo: 3 } };
    }).join();
    assert!(ret.is_err());
    unsafe { assert!(dropped); }
}


