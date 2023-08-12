tests/ui/duplicate/dupe-symbols-4.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

//
// error-pattern: symbol `fail` is already defined
#![crate_type="rlib"]
#![allow(warnings)]


pub trait A {
    fn fail(self);
}

struct B;
struct C;

impl A for B {
    #[no_mangle]
    fn fail(self) {}
}

impl A for C {
    #[no_mangle]
    fn fail(self) {}
}


