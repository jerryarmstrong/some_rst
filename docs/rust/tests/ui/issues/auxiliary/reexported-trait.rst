tests/ui/issues/auxiliary/reexported-trait.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod private {
    pub trait Trait {
        fn trait_method(&self) {
        }
    }
    pub trait TraitB {
        fn trait_method_b(&self) {
        }
    }
}

pub struct FooStruct;
pub use crate::private::Trait;
impl crate::private::Trait for FooStruct {}

pub use crate::private::TraitB as TraitBRename;
impl crate::private::TraitB for FooStruct {}


