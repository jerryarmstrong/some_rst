tests/ui/coherence/coherence-blanket-conflicts-with-specific-cross-crate.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:go_trait.rs

extern crate go_trait;

use go_trait::{Go,GoMut};
use std::fmt::Debug;
use std::default::Default;

struct MyThingy;

impl Go for MyThingy {
    fn go(&self, arg: isize) { }
}

impl GoMut for MyThingy {
//~^ ERROR E0119
    fn go_mut(&mut self, arg: isize) { }
}

fn main() { }


