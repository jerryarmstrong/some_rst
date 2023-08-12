sdk/program/src/borsh0_10.rs
============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![allow(clippy::integer_arithmetic)]
//! Utilities for the [borsh] serialization format, version 0.10.
//!
//! [borsh]: https://borsh.io/
use crate::borsh::{
    impl_get_instance_packed_len, impl_get_packed_len, impl_try_from_slice_unchecked,
};

impl_get_packed_len!(borsh);
impl_try_from_slice_unchecked!(borsh);
impl_get_instance_packed_len!(borsh);

#[cfg(test)]
mod tests {
    use crate::borsh::impl_tests;
    impl_tests!(borsh);
}


