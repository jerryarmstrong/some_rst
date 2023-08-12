tests/ui/coherence/impl[t]-foreign[local]-for-foreign[t].rs
===========================================================

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
struct Local1<S>(Rc<S>);

impl<T> Remote1<Local> for Rc<T> {}
impl<T, S> Remote1<Local1<S>> for Rc<T> {}

fn main() {}


