tests/ui/consts/const-needs_drop-monomorphic.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that evaluation of needs_drop<T> fails when T is not monomorphic.
#![feature(generic_const_exprs)]
#![allow(const_evaluatable_unchecked)]
#![allow(incomplete_features)]

struct Bool<const B: bool> {}
impl Bool<true> {
    fn assert() {}
}
fn f<T>() {
    Bool::<{ std::mem::needs_drop::<T>() }>::assert();
    //~^ ERROR no function or associated item named `assert` found
    //~| ERROR unconstrained generic constant
}
fn main() {
    f::<u32>();
}


