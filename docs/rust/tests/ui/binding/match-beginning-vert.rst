tests/ui/binding/match-beginning-vert.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
enum Foo {
    A,
    B,
    C,
    D,
    E,
}
use Foo::*;

fn main() {
    for foo in &[A, B, C, D, E] {
        match *foo {
            | A => println!("A"),
            | B | C if 1 < 2 => println!("BC!"),
            | _ => {},
        }
    }
}


