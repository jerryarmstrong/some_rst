tests/ui/lint/dead-code/trait-impl.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![deny(dead_code)]

enum Foo {
    Bar,
}

fn main() {
    let p = [0; 0];
    p.bar();
}

trait Bar {
    fn bar(&self) -> usize {
        3
    }
}

impl Bar for [u32; Foo::Bar as usize] {}


