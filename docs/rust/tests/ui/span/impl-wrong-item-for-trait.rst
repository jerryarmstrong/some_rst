tests/ui/span/impl-wrong-item-for-trait.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

trait Foo {
    fn bar(&self);
    const MY_CONST: u32;
}

pub struct FooConstForMethod;

impl Foo for FooConstForMethod {
    //~^ ERROR E0046
    const bar: u64 = 1;
    //~^ ERROR E0323
    const MY_CONST: u32 = 1;
}

pub struct FooMethodForConst;

impl Foo for FooMethodForConst {
    //~^ ERROR E0046
    fn bar(&self) {}
    fn MY_CONST() {}
    //~^ ERROR E0324
}

pub struct FooTypeForMethod;

impl Foo for FooTypeForMethod {
    //~^ ERROR E0046
    type bar = u64;
    //~^ ERROR E0325
    const MY_CONST: u32 = 1;
}

impl Debug for FooTypeForMethod {}
//~^ ERROR E0046

fn main() {}


