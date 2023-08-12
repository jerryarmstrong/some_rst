tests/ui/associated-inherent-types/normalize-projection-1.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(inherent_associated_types)]
#![allow(incomplete_features)]

struct S;

impl S {
    type P<T: O> = <T as O>::P;
}

trait O {
    type P;
}

impl O for i32 {
    type P = String;
}

fn main() {
    let _: S::P<i32> = String::new();
}


