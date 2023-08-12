tests/ui/consts/recursive.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]

const fn f<T>(x: T) { //~ WARN function cannot return without recursing
    f(x);
    //~^ ERROR evaluation of constant value failed
}

const X: () = f(1);

fn main() {}


