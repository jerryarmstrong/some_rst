tests/ui/type-alias-impl-trait/type_of_a_let.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![allow(dead_code)]

use std::fmt::Debug;

type Foo = impl Debug;

fn foo1() -> u32 {
    let x: Foo = 22_u32;
    x
}

fn foo2() -> u32 {
    let x: Foo = 22_u32;
    let y: Foo = x;
    same_type((x, y)); //~ ERROR use of moved value
    y //~ ERROR use of moved value
}

fn same_type<T>(x: (T, T)) {}

fn main() {}


