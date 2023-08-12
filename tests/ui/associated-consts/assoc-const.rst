tests/ui/associated-consts/assoc-const.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(associated_const_equality)]
#![allow(unused)]

pub trait Foo {
  const N: usize;
}

pub struct Bar;

impl Foo for Bar {
  const N: usize = 3;
}

const TEST:usize = 3;


fn foo<F: Foo<N=3usize>>() {}

fn main() {
  foo::<Bar>()
}


