tests/ui/issues/issue-36036-associated-type-layout.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue 36036: computing the layout of a type composed from another
// trait's associated type caused compiler to ICE when the associated
// type was allowed to be unsized, even though the known instantiated
// type is itself sized.

#![allow(dead_code)]

trait Context {
    type Container: ?Sized;
}

impl Context for u16 {
    type Container = u8;
}

struct Wrapper<C: Context+'static> {
    container: &'static C::Container
}

fn foobar(_: Wrapper<u16>) {}

static VALUE: u8 = 0;

fn main() {
    foobar(Wrapper { container: &VALUE });
}


