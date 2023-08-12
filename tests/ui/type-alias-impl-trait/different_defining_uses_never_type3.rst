tests/ui/type-alias-impl-trait/different_defining_uses_never_type3.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Tait = impl Sized;

struct One;
fn one() -> Tait { One }

struct Two<T>(T);
fn two() -> Tait { Two::<()>(todo!()) }
//~^ ERROR concrete type differs from previous defining opaque type use

fn main() {}


