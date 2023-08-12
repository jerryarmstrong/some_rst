tests/ui/object-safety/object-safety-no-static.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we correctly prevent users from making trait objects
// from traits with static methods.
//
// revisions: curr object_safe_for_dispatch

#![cfg_attr(object_safe_for_dispatch, feature(object_safe_for_dispatch))]

trait Foo {
    fn foo() {}
}

fn diverges() -> Box<dyn Foo> {
    //[curr]~^ ERROR E0038
    loop { }
}

struct Bar;

impl Foo for Bar {}

fn main() {
    let b: Box<dyn Foo> = Box::new(Bar);
    //[object_safe_for_dispatch]~^ ERROR E0038
}


