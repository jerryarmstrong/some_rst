tests/ui/auto-traits/typeck-default-trait-impl-negation.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

auto trait MyTrait {}

unsafe auto trait MyUnsafeTrait {}

struct ThisImplsTrait;

impl !MyUnsafeTrait for ThisImplsTrait {}


struct ThisImplsUnsafeTrait;

impl !MyTrait for ThisImplsUnsafeTrait {}

fn is_my_trait<T: MyTrait>() {}
fn is_my_unsafe_trait<T: MyUnsafeTrait>() {}

fn main() {
    is_my_trait::<ThisImplsTrait>();
    is_my_trait::<ThisImplsUnsafeTrait>();
    //~^ ERROR `ThisImplsUnsafeTrait: MyTrait` is not satisfied

    is_my_unsafe_trait::<ThisImplsTrait>();
    //~^ ERROR `ThisImplsTrait: MyUnsafeTrait` is not satisfied

    is_my_unsafe_trait::<ThisImplsUnsafeTrait>();
}


