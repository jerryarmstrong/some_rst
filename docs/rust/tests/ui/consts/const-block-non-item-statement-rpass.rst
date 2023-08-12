tests/ui/consts/const-block-non-item-statement-rpass.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code, unused)]

#[repr(u8)]
enum Foo {
    Bar = { let x = 1; 3 }
}

pub fn main() {
    assert_eq!(3, Foo::Bar as u8);
}


