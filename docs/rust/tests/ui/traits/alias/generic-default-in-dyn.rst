tests/ui/traits/alias/generic-default-in-dyn.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait SendEqAlias<T> = PartialEq;
//~^ ERROR trait aliases are experimental

struct Foo<T>(dyn SendEqAlias<T>);
//~^ ERROR the type parameter `Rhs` must be explicitly specified [E0393]

struct Bar<T>(dyn SendEqAlias<T>, T);
//~^ ERROR the type parameter `Rhs` must be explicitly specified [E0393]

fn main() {}


