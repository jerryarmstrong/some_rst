tests/ui/binding/pattern-in-closure.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_shorthand_field_patterns)]

struct Foo {
    x: isize,
    y: isize
}

pub fn main() {
    let f = |(x, _): (isize, isize)| println!("{}", x + 1);
    let g = |Foo { x: x, y: _y }: Foo| println!("{}", x + 1);
    f((2, 3));
    g(Foo { x: 1, y: 2 });
}


