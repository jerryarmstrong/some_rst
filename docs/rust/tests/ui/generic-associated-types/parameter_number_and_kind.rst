tests/ui/generic-associated-types/parameter_number_and_kind.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_type_defaults)]

trait Foo {
    type A<'a>;
    type B<'a, 'b>;
    type C;
    type D<T>;
    type E<'a, T>;
    // Test parameters in default values
    type FOk<T> = Self::E<'static, T>;
    type FErr1 = Self::E<'static, 'static>;
    //~^ ERROR this associated type takes 1 lifetime argument but 2 lifetime arguments were supplied
    //~| ERROR this associated type takes 1
    type FErr2<T> = Self::E<'static, T, u32>;
    //~^ ERROR this associated type takes 1
}

fn main() {}


