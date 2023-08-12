tests/ui/consts/const-for.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_for)]
#![feature(const_mut_refs)]

const _: () = {
    for _ in 0..5 {}
    //~^ error: cannot call
    //~| error: cannot convert
};

fn main() {}


