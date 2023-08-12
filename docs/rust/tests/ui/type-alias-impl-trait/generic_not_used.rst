tests/ui/type-alias-impl-trait/generic_not_used.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

type WrongGeneric<T: 'static> = impl 'static;
//~^ ERROR: at least one trait must be specified

fn wrong_generic<U: 'static, V: 'static>(_: U, v: V) -> WrongGeneric<U> {
    v
    //~^ ERROR type parameter `V` is part of concrete type but not used in parameter list
}


