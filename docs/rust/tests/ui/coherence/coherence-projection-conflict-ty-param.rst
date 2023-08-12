tests/ui/coherence/coherence-projection-conflict-ty-param.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Coherence error results because we do not know whether `T: Foo<P>` or not
// for the second impl.

use std::marker::PhantomData;

pub trait Foo<P> { fn foo() {} }

impl <P, T: Foo<P>> Foo<P> for Option<T> {}

impl<T, U> Foo<T> for Option<U> { }
//~^ ERROR E0119

fn main() {}


