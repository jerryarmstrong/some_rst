tests/ui/lint/dead-code/associated-type.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(dead_code)]

trait Foo {
    type Bar;
}

struct Used;

struct Ex;

impl Foo for Ex {
    type Bar = Used;
}

pub fn main() {
    let _x = Ex;
}


