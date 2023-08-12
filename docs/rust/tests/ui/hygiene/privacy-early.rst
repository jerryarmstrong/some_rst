tests/ui/hygiene/privacy-early.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![feature(decl_macro)]

mod foo {
    fn f() {}
    macro f() {}

    pub macro m() {
        use f as g; //~ ERROR `f` is private, and cannot be re-exported
        f!();
    }
}

fn main() {
    foo::m!();
}


