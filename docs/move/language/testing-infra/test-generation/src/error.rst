language/testing-infra/test-generation/src/error.rs
===================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use std::fmt;

/// This struct represents an error that is returned during the
/// testcase generation process.
#[derive(Debug)]
pub struct VMError {
    message: String,
}

impl VMError {
    pub fn new(message: String) -> VMError {
        VMError { message }
    }
}

impl fmt::Display for VMError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.message)
    }
}


