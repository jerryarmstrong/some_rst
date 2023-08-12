tests/rustdoc/auxiliary/async-trait-dep.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(async_fn_in_trait)]
#![allow(incomplete_features)]

pub trait Meow {
    /// Who's a good dog?
    async fn woof();
}


