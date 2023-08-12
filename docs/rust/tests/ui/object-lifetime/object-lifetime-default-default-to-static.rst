tests/ui/object-lifetime/object-lifetime-default-default-to-static.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that `Box<Test>` is equivalent to `Box<Test+'static>`, both in
// fields and fn arguments.

// pretty-expanded FIXME #23616

#![allow(dead_code)]

trait Test {
    fn foo(&self) { }
}

struct SomeStruct {
    t: Box<dyn Test>,
    u: Box<dyn Test+'static>,
}

fn a(t: Box<dyn Test>, mut ss: SomeStruct) {
    ss.t = t;
}

fn b(t: Box<dyn Test+'static>, mut ss: SomeStruct) {
    ss.t = t;
}

fn c(t: Box<dyn Test>, mut ss: SomeStruct) {
    ss.u = t;
}

fn d(t: Box<dyn Test+'static>, mut ss: SomeStruct) {
    ss.u = t;
}

fn main() {
}


