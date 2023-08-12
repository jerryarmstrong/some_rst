tests/ui/enum/enum-and-module-in-same-scope.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    X
}

mod Foo { //~ ERROR the name `Foo` is defined multiple times
    pub static X: isize = 42;
    fn f() { f() } // Check that this does not result in a resolution error
}

fn main() {}


