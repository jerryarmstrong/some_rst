tests/ui/pattern/usefulness/struct-like-enum-nonexhaustive.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A {
    B { x: Option<isize> },
    C
}

fn main() {
    let x = A::B { x: Some(3) };
    match x {   //~ ERROR non-exhaustive patterns
        A::C => {}
        A::B { x: None } => {}
    }
}


