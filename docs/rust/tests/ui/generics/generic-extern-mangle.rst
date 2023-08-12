tests/ui/generics/generic-extern-mangle.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::ops::Add;

extern "C" fn foo<T: Add>(a: T, b: T) -> T::Output { a + b }

fn main() {
    assert_eq!(100u8, foo(0u8, 100u8));
    assert_eq!(100u16, foo(0u16, 100u16));
}


