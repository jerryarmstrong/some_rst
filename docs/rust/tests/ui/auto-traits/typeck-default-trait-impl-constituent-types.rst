tests/ui/auto-traits/typeck-default-trait-impl-constituent-types.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

auto trait MyTrait {}

impl<T> !MyTrait for *mut T {}

struct MyS;

struct MyS2;

impl !MyTrait for MyS2 {}

struct MyS3;

fn is_mytrait<T: MyTrait>() {}

fn main() {
    is_mytrait::<MyS>();

    is_mytrait::<MyS2>();
    //~^ ERROR `MyS2: MyTrait` is not satisfied
}


