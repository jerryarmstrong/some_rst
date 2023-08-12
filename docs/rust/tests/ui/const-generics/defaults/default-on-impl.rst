tests/ui/const-generics/defaults/default-on-impl.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<const N: usize>;

impl<const N: usize = 1> Foo<N> {}
//~^ ERROR defaults for const parameters are only allowed

fn main() {}


