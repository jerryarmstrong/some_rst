tests/ui/union/union-generic.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

use std::rc::Rc;

union U<T: Copy> {
    a: T
}

fn main() {
    let u = U { a: Rc::new(0u32) };
    //~^ ERROR  the trait bound `Rc<u32>: Copy` is not satisfied
    let u = U::<Rc<u32>> { a: Default::default() };
    //~^ ERROR  the trait bound `Rc<u32>: Copy` is not satisfied
}


