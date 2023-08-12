nextest/fixtures/nextest-tests/src/lib.rs
=========================================

Last edited: 2022-02-01 05:13:53

Contents:

.. code-block:: rs

    // Copyright (c) The diem-devtools Contributors
// SPDX-License-Identifier: MIT OR Apache-2.0

#![allow(dead_code)]

/// This is a doctest.
///
/// ```
/// assert!(true, "this always succeeds");
/// ```
fn dummy_fn() {}

#[cfg(test)]
mod tests {
    #[test]
    fn unit_test_success() {
        assert_eq!(2 + 2, 4, "this test should succeed");
    }
}


