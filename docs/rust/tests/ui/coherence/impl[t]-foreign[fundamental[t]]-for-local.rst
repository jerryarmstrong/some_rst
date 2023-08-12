tests/ui/coherence/impl[t]-foreign[fundamental[t]]-for-local.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--crate-name=test
// aux-build:coherence_lib.rs
// check-pass

extern crate coherence_lib as lib;
use lib::*;
use std::rc::Rc;

struct Local;

impl<T> Remote1<Box<T>> for Local {}

impl<'a, T> Remote1<&'a T> for Local {}

fn main() {}


