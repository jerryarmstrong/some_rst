tests/ui/associated-consts/assoc-const-eq-missing.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_const_equality)]
#![allow(unused)]

pub trait Foo {
  const N: usize;
}

pub struct Bar;

impl Foo for Bar {
  const N: usize = 3;
}


fn foo1<F: Foo<Z=3>>() {}
//~^ ERROR associated type
fn foo2<F: Foo<Z=usize>>() {}
//~^ ERROR associated type
fn foo3<F: Foo<Z=5>>() {}
//~^ ERROR associated type

fn main() {
  foo1::<Bar>();
  foo2::<Bar>();
  foo3::<Bar>();
}


