tests/rustdoc/inline_cross/auxiliary/implementors_inline.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod my_trait {
    pub trait MyTrait {
        fn my_fn(&self) -> Self;
    }
}

pub mod prelude {
    #[doc(inline)]
    pub use crate::my_trait::MyTrait;
}

pub struct SomeStruct;

impl my_trait::MyTrait for SomeStruct {
    fn my_fn(&self) -> SomeStruct {
        SomeStruct
    }
}


