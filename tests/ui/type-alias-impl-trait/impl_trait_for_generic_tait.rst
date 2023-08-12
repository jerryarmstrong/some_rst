tests/ui/type-alias-impl-trait/impl_trait_for_generic_tait.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
trait Foo {
    type Assoc;
}

impl Foo for i32 {
    type Assoc = u32;
}
type ImplTrait = impl Sized;
fn constrain() -> ImplTrait {
    1u64
}
impl Foo for i64 {
    type Assoc = ImplTrait;
}

trait Bar<T> {}

impl<T: Foo> Bar<<T as Foo>::Assoc> for T {}

fn main() {}


