tests/ui/lint/lint-ctypes-73249-1.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![deny(improper_ctypes)]

pub trait Foo {
    type Assoc: 'static;
}

impl Foo for () {
    type Assoc = u32;
}

extern "C" {
    pub fn lint_me(x: Bar<()>);
}

#[repr(transparent)]
pub struct Bar<T: Foo> {
    value: &'static <T as Foo>::Assoc,
}

fn main() {}


