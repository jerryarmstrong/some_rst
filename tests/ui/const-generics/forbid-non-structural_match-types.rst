tests/ui/const-generics/forbid-non-structural_match-types.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(adt_const_params)]
#![allow(incomplete_features)]

#[derive(PartialEq, Eq)]
struct A;

struct B<const X: A>; // ok

struct C;

struct D<const X: C>; //~ ERROR `C` must be annotated with `#[derive(PartialEq, Eq)]`

fn main() {}


