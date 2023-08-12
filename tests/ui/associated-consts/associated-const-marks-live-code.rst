tests/ui/associated-consts/associated-const-marks-live-code.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(dead_code)]

const GLOBAL_BAR: u32 = 1;

struct Foo;

impl Foo {
    const BAR: u32 = GLOBAL_BAR;
}

pub fn main() {
    let _: u32 = Foo::BAR;
}


