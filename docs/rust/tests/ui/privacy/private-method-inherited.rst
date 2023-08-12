tests/ui/privacy/private-method-inherited.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that inherited visibility applies to methods.

mod a {
    pub struct Foo;

    impl Foo {
        fn f(self) {}
    }
}

fn main() {
    let x = a::Foo;
    x.f();  //~ ERROR associated function `f` is private
}


