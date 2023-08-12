tests/ui/generics/param-in-ct-in-ty-param-default.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T, U = [u8; std::mem::size_of::<T>()]>(T, U);
//~^ ERROR generic parameters may not be used in const operations

fn main() {}


