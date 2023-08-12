tests/ui/associated-consts/issue-102335-const.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_const_equality)]

trait T {
    type A: S<C<X = 0i32> = 34>;
    //~^ ERROR associated type bindings are not allowed here
}

trait S {
    const C: i32;
}

fn main() {}


