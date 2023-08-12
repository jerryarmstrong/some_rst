tests/rustdoc/intra-doc/auxiliary/extern-inherent-impl-dep.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
pub struct PublicStruct;

mod inner {
    use super::PublicStruct;

    impl PublicStruct {
        /// [PublicStruct::clone]
        pub fn method() {}
    }
}


