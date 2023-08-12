tests/ui/type-alias-impl-trait/missing_lifetime_bound.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Opaque<'a, T> = impl Sized;
fn defining<'a, T>(x: &'a i32) -> Opaque<T> { x }
//~^ ERROR: hidden type for `Opaque<'a, T>` captures lifetime that does not appear in bounds

fn main() {}


