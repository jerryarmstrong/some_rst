tests/ui/resolve/resolve-unknown-trait.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait NewTrait : SomeNonExistentTrait {}
//~^ ERROR cannot find trait `SomeNonExistentTrait` in this scope

impl SomeNonExistentTrait for isize {}
//~^ ERROR cannot find trait `SomeNonExistentTrait` in this scope

fn f<T:SomeNonExistentTrait>() {}
//~^ ERROR cannot find trait `SomeNonExistentTrait` in this scope

fn main() {}


