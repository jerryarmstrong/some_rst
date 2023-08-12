tests/ui/on-unimplemented/impl-substs.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

trait Foo<A> {
    fn foo(self);
}

#[rustc_on_unimplemented = "an impl did not match: {A} {B} {C}"]
impl<A, B, C> Foo<A> for (A, B, C) {
    fn foo(self) {}
}

fn main() {
    Foo::<usize>::foo((1i32, 1i32, 1i32));
    //~^ ERROR the trait bound `(i32, i32, i32): Foo<usize>` is not satisfied
}


