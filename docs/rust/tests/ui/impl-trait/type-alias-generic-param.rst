tests/ui/impl-trait/type-alias-generic-param.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #59342
// Checks that we properly detect defining uses of opaque
// types in 'item' position when generic parameters are involved
//
// run-pass
#![feature(type_alias_impl_trait)]

trait Meow {
    type MeowType;
    fn meow(self) -> Self::MeowType;
}

impl<T, I> Meow for I
where
    I: Iterator<Item = T>,
{
    type MeowType = impl Iterator<Item = T>;
    fn meow(self) -> Self::MeowType {
        self
    }
}

fn main() {}


