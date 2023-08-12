library/core/src/sync/mod.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Synchronization primitives

#![stable(feature = "rust1", since = "1.0.0")]

pub mod atomic;
mod exclusive;
#[unstable(feature = "exclusive_wrapper", issue = "98407")]
pub use exclusive::Exclusive;


