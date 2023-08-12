tests/ui/type-alias-impl-trait/generic_type_does_not_live_long_enough.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {
    let y = 42;
    let x = wrong_generic(&y);
    let z: i32 = x;
    //~^ ERROR expected generic type parameter, found `&'static i32
}

type WrongGeneric<T> = impl 'static;
//~^ ERROR: at least one trait must be specified

fn wrong_generic<T>(t: T) -> WrongGeneric<T> {
    t
    //~^ ERROR the parameter type `T` may not live long enough
}


