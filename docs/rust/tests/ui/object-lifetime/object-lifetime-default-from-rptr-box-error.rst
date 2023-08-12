tests/ui/object-lifetime/object-lifetime-default-from-rptr-box-error.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the lifetime from the enclosing `&` is "inherited"
// through the `Box` struct.

#![allow(dead_code)]

trait Test {
    fn foo(&self) { }
}

struct SomeStruct<'a> {
    t: &'a Box<dyn Test>,
}

fn c<'a>(t: &'a Box<dyn Test+'a>, mut ss: SomeStruct<'a>) {
    ss.t = t;
    //~^ ERROR lifetime may not live long enough
}

fn main() {
}


