tests/ui/coherence/impl-foreign-for-foreign[foreign].rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--crate-name=test
// aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::*;
use std::rc::Rc;

struct Local;

impl Remote1<Rc<i32>> for i32 {
    //~^ ERROR only traits defined in the current crate
    // | can be implemented for arbitrary types [E0117]
}
impl Remote1<Rc<Local>> for f64 {
    //~^ ERROR only traits defined in the current crate
    // | can be implemented for arbitrary types [E0117]
}
impl<T> Remote1<Rc<T>> for f32 {
    //~^ ERROR only traits defined in the current crate
    // | can be implemented for arbitrary types [E0117]
}

fn main() {}


