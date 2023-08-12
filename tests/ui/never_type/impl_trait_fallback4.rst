tests/ui/never_type/impl_trait_fallback4.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

trait T {
    type Assoc: Cake;
}

trait Cake: std::fmt::Display {
    fn cake() -> Self;
}

type Foo = impl T;

fn foo() -> impl T {
    //~^ ERROR `(): T` is not satisfied
    panic!()
}

fn a() -> Foo {
    foo()
}

fn main() {
    println!("{}", <Foo as T>::Assoc::cake());
}


