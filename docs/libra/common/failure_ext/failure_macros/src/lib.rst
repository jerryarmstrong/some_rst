common/failure_ext/failure_macros/src/lib.rs
============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Collection of convenience macros for error handling

/// Exits a function early with an `Error`.
///
/// Equivalent to the `bail!` macro, except a error type is provided instead of
/// a message.
#[macro_export]
macro_rules! bail_err {
    ($e:expr) => {
        return Err(From::from($e));
    };
}


