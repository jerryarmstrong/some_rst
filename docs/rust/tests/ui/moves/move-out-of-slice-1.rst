tests/ui/moves/move-out-of-slice-1.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_patterns)]

struct A;

fn main() {
    let a: Box<[A]> = Box::new([A]);
    match a { //~ ERROR cannot move out of type `[A]`, a non-copy slice
        box [a] => {},
        _ => {}
    }
}


