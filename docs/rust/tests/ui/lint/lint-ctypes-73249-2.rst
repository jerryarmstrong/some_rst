tests/ui/lint/lint-ctypes-73249-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

pub trait Baz {}

impl Baz for () {}

type Qux = impl Baz;

fn assign() -> Qux {}

pub trait Foo {
    type Assoc: 'static;
}

impl Foo for () {
    type Assoc = Qux;
}

#[repr(transparent)]
pub struct A<T: Foo> {
    x: &'static <T as Foo>::Assoc,
}

extern "C" {
    pub fn lint_me() -> A<()>; //~ ERROR: uses type `Qux`
}

fn main() {}


