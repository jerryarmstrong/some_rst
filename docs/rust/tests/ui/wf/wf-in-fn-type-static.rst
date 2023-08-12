tests/ui/wf/wf-in-fn-type-static.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we enforce WF conditions related to regions also for
// types in fns.

#![allow(dead_code)]


struct MustBeCopy<T:Copy> {
    t: T
}

struct Foo<T> {
    // needs T: 'static
    x: fn() -> &'static T //~ ERROR E0310
}

struct Bar<T> {
    // needs T: Copy
    x: fn(&'static T) //~ ERROR E0310
}


fn main() { }


