tests/ui/lint/lint-ctypes-73251-1.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

pub trait Baz {}

impl Baz for u32 {}

type Qux = impl Baz;

pub trait Foo {
    type Assoc;
}

impl Foo for u32 {
    type Assoc = Qux;
}

fn assign() -> Qux {
    1
}

extern "C" {
    pub fn lint_me() -> <u32 as Foo>::Assoc; //~ ERROR: uses type `Qux`
}

fn main() {}


