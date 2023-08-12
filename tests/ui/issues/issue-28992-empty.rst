tests/ui/issues/issue-28992-empty.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Can't use constants as tuple struct patterns


const C1: i32 = 0;

struct S;

impl S {
    const C2: i32 = 0;
}

fn main() {
    if let C1(..) = 0 {} //~ ERROR expected tuple struct or tuple variant, found constant `C1`
    if let S::C2(..) = 0 {}
    //~^ ERROR expected tuple struct or tuple variant, found associated constant `S::C2`
}


