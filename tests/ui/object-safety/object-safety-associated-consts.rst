tests/ui/object-safety/object-safety-associated-consts.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we correctly prevent users from making trait objects
// from traits with associated consts.
//
// revisions: curr object_safe_for_dispatch

#![cfg_attr(object_safe_for_dispatch, feature(object_safe_for_dispatch))]

trait Bar {
    const X: usize;
}

fn make_bar<T:Bar>(t: &T) -> &dyn Bar {
    //[curr]~^ ERROR E0038
    t
    //[object_safe_for_dispatch]~^ ERROR E0038
}

fn main() {
}


