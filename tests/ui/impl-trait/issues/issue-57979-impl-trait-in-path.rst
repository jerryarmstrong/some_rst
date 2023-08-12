tests/ui/impl-trait/issues/issue-57979-impl-trait-in-path.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rust-lang/rust#57979 : the initial support for `impl Trait` didn't
// properly check syntax hidden behind an associated type projection.
// Here we test behavior of occurrences of `impl Trait` within a path
// component in that context.

pub trait Bar { }
pub trait Quux<T> { type Assoc; }
pub fn demo(_: impl Quux<(), Assoc=<() as Quux<impl Bar>>::Assoc>) { }
//~^ ERROR `impl Trait` is not allowed in path parameters
impl<T> Quux<T> for () { type Assoc = u32; }

fn main() { }


