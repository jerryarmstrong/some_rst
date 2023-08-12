tests/ui/traits/impl_trait_as_trait_return_position.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait A {
    type Foo;
}

impl<T> A for T {
    type Foo = ();
}

fn foo() -> impl std::borrow::Borrow<<u8 as A>::Foo> {
    ()
}

fn main() {
    foo();
}


