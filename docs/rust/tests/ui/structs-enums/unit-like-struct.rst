tests/ui/structs-enums/unit-like-struct.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo;

pub fn main() {
    let x: Foo = Foo;
    match x {
        Foo => { println!("hi"); }
    }
}


