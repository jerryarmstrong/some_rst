tests/ui/rfc-2632-const-trait-impl/non-const-op-in-closure-in-const.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl)]

#[const_trait]
trait Convert<T> {
    fn to(self) -> T;
}

impl<A, B> const Convert<B> for A where B: ~const From<A> {
    fn to(self) -> B {
        B::from(self)
    }
}

const FOO: fn() -> String = || "foo".to();

fn main() {}


