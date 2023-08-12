tests/rustdoc/inline_cross/auxiliary/impl-inline-without-trait.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait MyTrait {
    /// docs for my_trait_method
    fn my_trait_method() {}
}

pub struct MyStruct;

impl MyTrait for MyStruct {}


