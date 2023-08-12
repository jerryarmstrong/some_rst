tests/ui/nll/relate_tys/opaque-hrtb.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait MyTrait<T> {}

struct Foo;
impl<T> MyTrait<T> for Foo {}

fn bar<Input>() -> impl MyTrait<Input> {
    Foo
}

fn foo() -> impl for<'a> MyTrait<&'a str> {
    bar() //~ ERROR implementation of `MyTrait` is not general enough
}

fn main() {}


