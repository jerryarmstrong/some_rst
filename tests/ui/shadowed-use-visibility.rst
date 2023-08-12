tests/ui/shadowed-use-visibility.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
mod foo {
    pub fn f() {}

    pub use self::f as bar;
    use foo as bar;
}

fn main() {
    foo::bar();
}


