tests/ui/packed/packed-struct-borrow-element.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass (note: this is spec-UB, but it works for now)
#![allow(dead_code)]
// ignore-emscripten weird assertion?

#[repr(packed)]
struct Foo1 {
    bar: u8,
    baz: usize
}

#[repr(packed(2))]
struct Foo2 {
    bar: u8,
    baz: usize
}

#[repr(C, packed(4))]
struct Foo4C {
    bar: u8,
    baz: usize
}

#[warn(unaligned_references)]
pub fn main() {
    let foo = Foo1 { bar: 1, baz: 2 };
    let brw = &foo.baz; //~WARN reference to packed field is unaligned
    //~^ previously accepted
    assert_eq!(*brw, 2);

    let foo = Foo2 { bar: 1, baz: 2 };
    let brw = &foo.baz; //~WARN reference to packed field is unaligned
    //~^ previously accepted
    assert_eq!(*brw, 2);
}


