tests/ui/const-generics/unused_braces.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// run-rustfix
#![warn(unused_braces)]

macro_rules! make_1 {
    () => {
        1
    }
}

struct A<const N: usize>;

fn main() {
    let _: A<7>; // ok
    let _: A<{ 7 }>; //~ WARN unnecessary braces
    let _: A<{ 3 + 5 }>; // ok
    let _: A<{make_1!()}>; // ok
}


