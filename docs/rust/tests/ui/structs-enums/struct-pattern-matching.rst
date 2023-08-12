tests/ui/structs-enums/struct-pattern-matching.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_shorthand_field_patterns)]

struct Foo {
    x: isize,
    y: isize,
}

pub fn main() {
    let a = Foo { x: 1, y: 2 };
    match a {
        Foo { x: x, y: y } => println!("yes, {}, {}", x, y)
    }

    match a {
        Foo { .. } => ()
    }
}


