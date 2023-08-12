tests/ui/type-alias-impl-trait/generic_underconstrained2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

type Underconstrained<T: std::fmt::Debug> = impl Send;

// not a defining use, because it doesn't define *all* possible generics
fn underconstrained<U>(_: U) -> Underconstrained<U> {
    //~^ ERROR `U` doesn't implement `Debug`
    5u32
}

type Underconstrained2<T: std::fmt::Debug> = impl Send;

// not a defining use, because it doesn't define *all* possible generics
fn underconstrained2<U, V>(_: U, _: V) -> Underconstrained2<V> {
    //~^ ERROR `V` doesn't implement `Debug`
    5u32
}


