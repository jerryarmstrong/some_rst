tests/ui/infinite/infinite-trait-alias-recursion.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

trait T1 = T2;
//~^ ERROR cycle detected when computing the super predicates of `T1`

trait T2 = T3;

trait T3 = T1 + T3;

fn main() {}


