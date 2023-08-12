tests/ui/pattern/usefulness/struct-pattern-match-useless.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

struct Foo {
    x: isize,
    y: isize,
}

pub fn main() {
    let a = Foo { x: 1, y: 2 };
    match a {
        Foo { x: _x, y: _y } => (),
        Foo { .. } => () //~ ERROR unreachable pattern
    }

}


