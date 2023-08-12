tests/ui/coherence/coherence-multidispatch-tuple.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]
// pretty-expanded FIXME #23616

use std::fmt::Debug;
use std::default::Default;

// Test that an impl for homogeneous pairs does not conflict with a
// heterogeneous pair.

trait MyTrait {
    fn get(&self) -> usize;
}

impl<T> MyTrait for (T,T) {
    fn get(&self) -> usize { 0 }
}

impl MyTrait for (usize,isize) {
    fn get(&self) -> usize { 0 }
}

fn main() {
}


