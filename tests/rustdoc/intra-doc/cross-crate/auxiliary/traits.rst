tests/rustdoc/intra-doc/cross-crate/auxiliary/traits.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "inner"]
/// this is a trait
pub trait SomeTrait {
    /// this is a method for [a trait][SomeTrait]
    fn foo();
}

pub mod bar {
    use super::SomeTrait;

    pub struct BarStruct;

    impl SomeTrait for BarStruct {
        fn foo() {}
    }
}


