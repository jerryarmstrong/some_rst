tests/ui/associated-consts/assoc-const-ty-mismatch.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_const_equality)]
#![allow(unused)]

pub trait Foo {
  const N: usize;
}

pub trait FooTy {
  type T;
}

pub struct Bar;

impl Foo for Bar {
  const N: usize = 3;
}

impl FooTy for Bar {
  type T = usize;
}


fn foo<F: Foo<N=usize>>() {}
//~^ ERROR expected associated constant bound, found type
fn foo2<F: FooTy<T=3usize>>() {}
//~^ ERROR expected associated type bound, found constant

fn main() {
  foo::<Bar>();
  foo2::<Bar>();
}


