tests/ui/array-slice-vec/slice-panic-2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind

// ignore-emscripten no threads support

// Test that if a slicing expr[..] fails, the correct cleanups happen.


use std::thread;

struct Foo;

static mut DTOR_COUNT: isize = 0;

impl Drop for Foo {
    fn drop(&mut self) { unsafe { DTOR_COUNT += 1; } }
}

fn bar() -> usize {
    panic!();
}

fn foo() {
    let x: &[_] = &[Foo, Foo];
    let _ = &x[3..bar()];
}

fn main() {
    let _ = thread::spawn(move|| foo()).join();
    unsafe { assert_eq!(DTOR_COUNT, 2); }
}


