tests/ui/issues/auxiliary/issue-9968.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use internal::core::{Trait, Struct};

mod internal {
    pub mod core {
        pub struct Struct;
        impl Struct {
            pub fn init() -> Struct {
                Struct
            }
        }

        pub trait Trait {
            fn test(&self) {
                private();
            }
        }

        impl Trait for Struct {}

        fn private() { }
    }
}


