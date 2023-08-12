tests/ui/numbers-arithmetic/int-abs-overflow.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -C overflow-checks=on
// ignore-emscripten no threads support
// needs-unwind

use std::thread;

fn main() {
    assert!(thread::spawn(|| i8::MIN.abs()).join().is_err());
    assert!(thread::spawn(|| i16::MIN.abs()).join().is_err());
    assert!(thread::spawn(|| i32::MIN.abs()).join().is_err());
    assert!(thread::spawn(|| i64::MIN.abs()).join().is_err());
    assert!(thread::spawn(|| isize::MIN.abs()).join().is_err());
}


