tests/ui/suggestions/suggest-swapping-self-ty-and-trait-edition-2021.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

pub trait Trait<'a, T> {}

pub struct Struct<T>;
pub enum Enum<T> {}

pub union Union<T> {
    f1: usize,
}

impl<'a, T> Struct<T> for Trait<'a, T> {}
//~^ ERROR expected trait, found struct `Struct`
//~| ERROR trait objects must include the `dyn` keyword

impl<'a, T> Enum<T> for Trait<'a, T> {}
//~^ ERROR expected trait, found enum `Enum`

impl<'a, T> Union<T> for Trait<'a, T> {}
//~^ ERROR expected trait, found union `Union`

fn main() {}


