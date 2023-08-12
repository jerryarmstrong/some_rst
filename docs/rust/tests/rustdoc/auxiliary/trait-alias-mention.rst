tests/rustdoc/auxiliary/trait-alias-mention.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

pub trait SomeAlias = std::fmt::Debug + std::marker::Copy;


