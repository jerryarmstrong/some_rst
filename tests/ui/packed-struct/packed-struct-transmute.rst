tests/ui/packed-struct/packed-struct-transmute.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This assumes the packed and non-packed structs are different sizes.

// the error points to the start of the file, not the line with the
// transmute

// normalize-stderr-test "\d+ bits" -> "N bits"
// error-pattern: cannot transmute between types of different sizes, or dependently-sized types

use std::mem;

#[repr(packed)]
struct Foo {
    bar: u8,
    baz: usize
}

#[derive(Debug)]
struct Oof {
    rab: u8,
    zab: usize
}

fn main() {
    let foo = Foo { bar: 1, baz: 10 };
    unsafe {
        let oof: Oof = mem::transmute(foo);
        println!("{:?}", oof);
    }
}


