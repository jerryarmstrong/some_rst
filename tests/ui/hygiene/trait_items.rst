tests/ui/hygiene/trait_items.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod foo {
    pub trait T {
        fn f(&self) {}
    }
    impl T for () {}
}

mod bar {
    use foo::*;
    pub macro m() { ().f() }
    fn f() { ::baz::m!(); }
}

mod baz {
    pub macro m() { ().f() } //~ ERROR no method named `f` found
    fn f() { ::bar::m!(); }
}

fn main() {}


