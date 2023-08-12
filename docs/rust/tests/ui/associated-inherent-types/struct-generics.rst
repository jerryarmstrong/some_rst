tests/ui/associated-inherent-types/struct-generics.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(inherent_associated_types)]
#![allow(incomplete_features)]

struct S<T>(T);

impl<T> S<T> {
    type P = T;
}

fn main() {
    type A = S<()>::P;
    let _: A = ();
}


