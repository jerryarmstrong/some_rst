tests/ui/hygiene/auxiliary/xcrate.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]
#![allow(unused)]

pub use bar::test;

extern crate std as foo;

pub fn f() {}
use f as f2;

mod bar {
    pub fn g() {}
    use baz::h;

    pub macro test() {
        use std::mem;
        use foo::cell;
        ::f();
        ::f2();
        g();
        h();
        ::bar::h();
    }
}

mod baz {
    pub fn h() {}
}


