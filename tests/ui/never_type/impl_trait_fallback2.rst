tests/ui/never_type/impl_trait_fallback2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

trait T {}
impl T for i32 {}

fn should_ret_unit() -> impl T {
    //~^ ERROR `(): T` is not satisfied
    panic!()
}

type Foo = impl T;

fn a() -> Foo {
    //~^ ERROR `(): T` is not satisfied
    panic!()
}

fn b() -> Foo {
    42
}


