tests/ui/type-alias-impl-trait/assoc-type-lifetime-unconstrained.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we don't allow unconstrained lifetime parameters in impls when
// the lifetime is used in an associated opaque type.

#![feature(type_alias_impl_trait)]

trait UnwrapItemsExt {
    type Iter;
    fn unwrap_items(self) -> Self::Iter;
}

struct MyStruct {}

trait MyTrait<'a> {}

impl<'a> MyTrait<'a> for MyStruct {}

impl<'a, I> UnwrapItemsExt for I {
    //~^ ERROR the lifetime parameter `'a` is not constrained
    type Iter = impl MyTrait<'a>;

    fn unwrap_items(self) -> Self::Iter {
        MyStruct {}
    }
}

fn main() {}


