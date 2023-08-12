tests/ui/coherence/coherence-blanket-conflicts-with-blanket-implemented.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;
use std::default::Default;

// Test that two blanket impls conflict (at least without negative
// bounds).  After all, some other crate could implement Even or Odd
// for the same type (though this crate doesn't).

trait MyTrait {
    fn get(&self) -> usize;
}

trait Even { }

trait Odd { }

impl Even for isize { }

impl Odd for usize { }

impl<T:Even> MyTrait for T {
    fn get(&self) -> usize { 0 }
}

impl<T:Odd> MyTrait for T {
//~^ ERROR E0119

    fn get(&self) -> usize { 0 }
}

fn main() { }


