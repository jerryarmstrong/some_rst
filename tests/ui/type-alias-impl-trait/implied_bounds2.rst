tests/ui/type-alias-impl-trait/implied_bounds2.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

type Ty<'a, A> = impl Sized + 'a;
fn defining<'a, A>() -> Ty<'a, A> {}
fn assert_static<T: 'static>() {}
fn test<'a, A>() where Ty<'a, A>: 'static, { assert_static::<Ty<'a, A>>() }

fn main() {}


