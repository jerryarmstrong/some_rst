tests/ui/type-alias-impl-trait/generic_different_defining_uses.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

type MyIter<T> = impl Iterator<Item = T>;

fn my_iter<T>(t: T) -> MyIter<T> {
    std::iter::once(t)
}

fn my_iter2<T>(t: T) -> MyIter<T> {
    Some(t).into_iter()
    //~^ ERROR concrete type differs from previous
}


