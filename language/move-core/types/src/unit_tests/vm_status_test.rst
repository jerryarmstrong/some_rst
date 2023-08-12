language/move-core/types/src/unit_tests/vm_status_test.rs
=========================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::vm_status::{StatusCode, VMStatus};

#[test]
fn test_stats_code() {
    let vm_status = VMStatus::Error(StatusCode::OUT_OF_GAS);
    let code = vm_status.status_code();
    assert_eq!(code, StatusCode::OUT_OF_GAS);
}


