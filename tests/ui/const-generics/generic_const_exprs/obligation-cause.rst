tests/ui/const-generics/generic_const_exprs/obligation-cause.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(incomplete_features)]
#![feature(generic_const_exprs)]

trait True {}

struct Is<const V: bool>;

impl True for Is<true> {}

fn g<T>()
//~^ NOTE required by a bound in this
where
    Is<{ std::mem::size_of::<T>() == 0 }>: True,
    //~^ NOTE required by a bound in `g`
    //~| NOTE required by this bound in `g`
{
}

fn main() {
    g::<usize>();
    //~^ ERROR mismatched types
    //~| NOTE expected `false`, found `true`
    //~| NOTE expected constant `false`
}


