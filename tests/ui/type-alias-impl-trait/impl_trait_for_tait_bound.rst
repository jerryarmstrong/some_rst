tests/ui/type-alias-impl-trait/impl_trait_for_tait_bound.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

use std::fmt::Debug;

type Foo = impl Debug;
pub trait Yay { }
impl Yay for Foo { }

fn foo() {
    is_yay::<u32>();   //~ ERROR: the trait bound `u32: Yay` is not satisfied
    is_debug::<u32>(); // OK
    is_yay::<Foo>();   // OK
    is_debug::<Foo>(); // OK
}

fn is_yay<T: Yay>() { }
fn is_debug<T: Debug>() { }

fn main() {}


