tests/ui/impl-trait/issues/issue-57979-nested-impl-trait-in-assoc-proj.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rust-lang/rust#57979 : the initial support for `impl Trait` didn't
// properly check syntax hidden behind an associated type projection.
// Here we test behavior of occurrences of `impl Trait` within an
// `impl Trait` in that context.

pub trait Foo<T> { }
pub trait Bar { }
pub trait Quux { type Assoc; }
pub fn demo(_: impl Quux<Assoc=impl Foo<impl Bar>>) { }
//~^ ERROR nested `impl Trait` is not allowed

fn main() { }


