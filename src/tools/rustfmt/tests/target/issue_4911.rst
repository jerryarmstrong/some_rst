src/tools/rustfmt/tests/target/issue_4911.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(min_type_alias_impl_trait)]

impl SomeTrait for SomeType {
    type SomeGAT<'a>
    where
        Self: 'a,
    = impl SomeOtherTrait;
}


