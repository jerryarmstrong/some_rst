tests/ui/pub/issue-33174-restricted-type-in-public-interface.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_camel_case_types)] // genus is always capitalized

pub(crate) struct Snail;
//~^ NOTE `Snail` declared as private

mod sea {
    pub(super) struct Turtle;
    //~^ NOTE `Turtle` declared as crate-private
}

struct Tortoise;
//~^ NOTE `Tortoise` declared as private

pub struct Shell<T> {
    pub(crate) creature: T,
}

pub type Helix_pomatia = Shell<Snail>;
//~^ ERROR private type `Snail` in public interface
//~| NOTE can't leak private type
pub type Dermochelys_coriacea = Shell<sea::Turtle>;
//~^ ERROR crate-private type `Turtle` in public interface
//~| NOTE can't leak crate-private type
pub type Testudo_graeca = Shell<Tortoise>;
//~^ ERROR private type `Tortoise` in public interface
//~| NOTE can't leak private type

fn main() {}


