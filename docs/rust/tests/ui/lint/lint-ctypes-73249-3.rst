tests/ui/lint/lint-ctypes-73249-3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![deny(improper_ctypes)]

pub trait Baz {}

impl Baz for u32 {}

type Qux = impl Baz;

fn assign() -> Qux {
    3
}

#[repr(C)]
pub struct A {
    x: Qux,
}

extern "C" {
    pub fn lint_me() -> A; //~ ERROR: uses type `Qux`
}

fn main() {}


