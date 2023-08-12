tests/ui/type-alias-impl-trait/impl_trait_for_tait_bound2.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

use std::fmt::Debug;

type Foo = impl Debug;

pub trait Yay { }
impl Yay for u32 { }

fn foo() {
    is_yay::<Foo>(); //~ ERROR: the trait bound `Foo: Yay` is not satisfied
}

fn is_yay<T: Yay>() { }

fn main() {}


