tests/ui/did_you_mean/issue-46718-struct-pattern-dotdotdot.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]

struct PersonalityInventory {
    expressivity: f32,
    instrumentality: f32
}

impl PersonalityInventory {
    fn expressivity(&self) -> f32 {
        match *self {
            PersonalityInventory { expressivity: exp, ... } => exp
            //~^ ERROR expected field pattern, found `...`
        }
    }
}

fn main() {}


