tests/ui/coherence/impl[t]-foreign[foreign[t]_local]-for-foreign.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--crate-name=test
// aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::*;
use std::rc::Rc;

struct Local;
impl<T> Remote2<Rc<T>, Local> for usize { }

fn main() {}


