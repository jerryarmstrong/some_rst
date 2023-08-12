tests/ui/type-alias-impl-trait/argument-types.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![allow(dead_code)]
// check-pass
use std::fmt::Debug;

type Foo = impl Debug;

fn foo1(mut x: Foo) {
    x = 22_u32;
}

fn foo2(mut x: Foo) {
    // no constraint on x
}

fn foo3(x: Foo) {
    println!("{:?}", x);
}

fn foo_value() -> Foo {
    11_u32
}

fn main() {
    foo3(foo_value());
}


