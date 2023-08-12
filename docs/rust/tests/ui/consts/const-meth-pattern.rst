tests/ui/consts/const-meth-pattern.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct A;

impl A {
    const fn banana() -> bool {
        true
    }
}

const ABANANA: bool = A::banana();

fn main() {
    match true {
        ABANANA => {},
        _ => panic!("what?")
    }
}


