tests/ui/consts/const-size_of-cycle.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: cycle detected

struct Foo {
    bytes: [u8; std::mem::size_of::<Foo>()]
}

fn main() {}


