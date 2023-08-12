tests/ui/lint/lint-ctypes-73251.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

pub trait Foo {
    type Assoc;
}

impl Foo for () {
    type Assoc = u32;
}

type Bar = impl Foo<Assoc = u32>;

fn assign() -> Bar {}

extern "C" {
    pub fn lint_me() -> <Bar as Foo>::Assoc;
}

fn main() {}


