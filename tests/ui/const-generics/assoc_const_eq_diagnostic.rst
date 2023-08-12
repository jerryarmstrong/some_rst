tests/ui/const-generics/assoc_const_eq_diagnostic.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_const_equality)]

pub enum Mode {
    Cool,
}

pub trait Parse {
    const MODE: Mode;
}

pub trait CoolStuff: Parse<MODE = Mode::Cool> {}
//~^ ERROR expected associated constant bound
//~| ERROR expected type

fn no_help() -> Mode::Cool {}
//~^ ERROR expected type, found variant

fn main() {}


