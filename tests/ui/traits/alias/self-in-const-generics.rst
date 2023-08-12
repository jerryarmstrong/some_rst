tests/ui/traits/alias/self-in-const-generics.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(incomplete_features)]
#![feature(generic_const_exprs)]
#![feature(trait_alias)]

trait Bar<const N: usize> {}

trait BB = Bar<{ 2 + 1 }>;

fn foo(x: &dyn BB) {}
//~^ ERROR the trait alias `BB` cannot be made into an object [E0038]

fn main() {}


