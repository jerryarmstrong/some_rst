tests/ui/consts/const-eval/extern_fat_pointer.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(extern_types)]

extern "C" {
    type Opaque;
}

const FOO: *const u8 = &42 as *const _ as *const Opaque as *const u8;

fn main() {
    let _foo = FOO;
}


