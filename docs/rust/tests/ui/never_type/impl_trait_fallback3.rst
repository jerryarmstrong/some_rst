tests/ui/never_type/impl_trait_fallback3.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

trait T {
    type Assoc;
}

type Foo = impl T;

fn a() -> Foo {
    //~^ ERROR the trait bound `(): T` is not satisfied
    // This is not a defining use, it doesn't actually constrain the opaque type.
    panic!()
}


