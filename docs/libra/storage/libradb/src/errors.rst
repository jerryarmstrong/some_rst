storage/libradb/src/errors.rs
=============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines error types used by [`LibraDB`](crate::LibraDB).

use failure::Fail;

/// This enum defines errors commonly used among [`LibraDB`](crate::LibraDB) APIs.
#[derive(Debug, Fail)]
pub enum LibraDbError {
    /// A requested item is not found.
    #[fail(display = "{} not found.", _0)]
    NotFound(String),
    /// Requested too many items.
    #[fail(display = "Too many items requested: {}, max is {}", _0, _1)]
    TooManyRequested(u64, u64),
}


