tests/ui/type-alias-impl-trait/assoc-type-const.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we properly detect defining usages when using
// const generics in an associated opaque type
// check-pass

#![feature(type_alias_impl_trait)]

trait UnwrapItemsExt<'a, const C: usize> {
    type Iter;
    fn unwrap_items(self) -> Self::Iter;
}

struct MyStruct<const C: usize> {}

trait MyTrait<'a, const C: usize> {
    type MyItem;
    const MY_CONST: usize;
}

impl<'a, const C: usize> MyTrait<'a, C> for MyStruct<C> {
    type MyItem = u8;
    const MY_CONST: usize = C;
}

impl<'a, I, const C: usize> UnwrapItemsExt<'a, C> for I {
    type Iter = impl MyTrait<'a, C>;

    fn unwrap_items(self) -> Self::Iter {
        MyStruct::<C> {}
    }
}

fn main() {}


