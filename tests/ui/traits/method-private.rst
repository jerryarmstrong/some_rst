tests/ui/traits/method-private.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod inner {
    pub trait Bar {
        fn method(&self);
    }

    pub struct Foo;

    impl Foo {
        fn method(&self) {}
    }

    impl Bar for Foo {
        fn method(&self) {}
    }
}

fn main() {
    let foo = inner::Foo;
    foo.method(); //~ ERROR is private
}


