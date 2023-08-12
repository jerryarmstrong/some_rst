tests/ui/consts/const-unsafe-fn.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// A quick test of 'unsafe const fn' functionality

const unsafe fn dummy(v: u32) -> u32 {
    !v
}

struct Type;
impl Type {
    const unsafe fn new() -> Type {
        Type
    }
}

const VAL: u32 = unsafe { dummy(0xFFFF) };
const TYPE_INST: Type = unsafe { Type::new() };

fn main() {
    assert_eq!(VAL, 0xFFFF0000);
}


